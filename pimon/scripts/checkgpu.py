
def reset_gpio(rig):
    import RPi.GPIO as GPIO
    import time
    GPIO.setwarnings(False)
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    #Setup GPIO
    GPIO.setup(rig.gpio, GPIO.OUT)
    #Turn Off Rig/Hold Reset (Send LOW)
    GPIO.output(rig.gpio, GPIO.LOW)
    time.sleep(1)
    #Turn On Rig/Release Reset (Send HIGH)
    GPIO.output(rig.gpio, GPIO.HIGH)
    #Cleanup
    GPIO.cleanup()

def check_gpu(gpu):
    import socket
    import json
    import pytz 
    from datetime import tzinfo, timedelta, datetime
    from pimon.models import ConfigGlobal, Myrig
    timeZone = ConfigGlobal.objects.filter(pk=1)[0].timezone
    tempCheck = False
    hashCheck = False
    onlineCheck = False
    if gpu.software == 'ethminer':
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        try:
            s.connect((gpu.address, gpu.port))
            s.send('{"id":0,"jsonrpc":"2.0","method":"miner_getstat1","psw":"' + gpu.passw + '"}'.encode("utf-8"))
            j = s.recv(2048)
            s.close()
            res = json.loads(j.decode("utf-8"))
            res = res['result']
            hashCheck = (gpu.hashr/1000) < int(res[2].split(';')[0])
            x = int('0')
            onlineCheck = True
            for gpuTemp in res[6].split(';'):
                if x < int(len(res[6].split(';'))-1):
                    if x % 2 == 0:
                        tempCheck = gpu.temp > int(gpuTemp)
                        x=x+1
                    elif x % 2 != 0:
                        x=x+1
                    else:
                        break
                elif x >= int(len(res[6].split(';'))-1):
                    break      
                else:
                    break
            return onlineCheck, hashCheck, tempCheck
        except socket.error:
            return onlineCheck, hashCheck, tempCheck
        return onlineCheck, hashCheck, tempCheck
    elif (gpu.software == 'ccminer' or gpu.software == 'cgminer' or gpu.software == 'sgminer' or 
            gpu.software == 'bgminer' or gpu.software == 'bmminer' or gpu.software == 'bfgminer'):
        return datetime.now(tz=pytz.timezone(timeZone)).strftime('[%m-%d-%Y %H:%M:%S]: ') + 'Reset feature not yet available for software used for ' + gpu.name + '.'
    elif gpu.software == 'NONE':
        return datetime.now(tz=pytz.timezone(timeZone)).strftime('[%m-%d-%Y %H:%M:%S]: ') + 'Software not defined in Myrig Profile for ' + gpu.name + '. Please correct.'
    else:
        return datetime.now(tz=pytz.timezone(timeZone)).strftime('[%m-%d-%Y %H:%M:%S]: ') + 'Unable to process GPU check for ' + gpu.name + '. [Err 0]'

def result_zero_gpu(rig):
    import pytz 
    from datetime import tzinfo, timedelta, datetime
    from pimon.scripts.utils import pretty_date
    from pimon.models import ConfigGlobal, Myrig
    timeZone = ConfigGlobal.objects.filter(pk=1)[0].timezone
    if rig.statustime == None:
        if rig.resettime == None:
            rigSave = Myrig.objects.get(name=rig.name)
            if rig.resetcounter == 0:
                rigSave.firststatus = datetime.now(tz=pytz.timezone(timeZone))
            rigSave.statustime = datetime.now(tz=pytz.timezone(timeZone))
            rigSave.save()
            print datetime.now(tz=pytz.timezone(timeZone)).strftime('[%m-%d-%Y %H:%M:%S]: ') + str(rig.name) + ' detected Unreachable/Offline.'
            return None, None, None
        else:
            dTime = datetime.now(tz=pytz.timezone(timeZone)) - rig.resettime
            if dTime >= timedelta(minutes=ConfigGlobal.objects.filter(pk=1)[0].gpuresetwait):
                if rig.resetcounter < ConfigGlobal.objects.filter(pk=1)[0].gpuresetattempts:
                    rigSave = Myrig.objects.get(name=rig.name)
                    rigSave.resettime = None
                    rigSave.save()
                    print datetime.now(tz=pytz.timezone(timeZone)).strftime('[%m-%d-%Y %H:%M:%S]: ') + 'It has been ' '{:.0f}'.format(ConfigGlobal.objects.filter(pk=1)[0].gpuresetwait) + ' minutes, resetting timers for ' + str(rig.name) + '.'
                    return None, None, None
                else:
                    print datetime.now(tz=pytz.timezone(timeZone)).strftime('[%m-%d-%Y %H:%M:%S]: ') + 'The rig ' + str(rig.name) + ' has been reset ' + str(rig.resetcounter) + ' times and remains unreachable since ' + str(pretty_date(rig.firststatus)) + str(rig.firststatus.strftime(' [%m-%d-%Y %H:%M:%S]')) + '.'
                    return None, None, None
            else:
                print datetime.now(tz=pytz.timezone(timeZone)).strftime('[%m-%d-%Y %H:%M:%S]: ') + 'The reset wait timer has not expired yet for ' + str(rig.name) + '.'
                return None, None, None
    else:
        dTime = datetime.now(tz=pytz.timezone(timeZone)) - rig.statustime
        if dTime >= timedelta(minutes=ConfigGlobal.objects.filter(pk=1)[0].gpureset):
            if rig.email == 'yes' and rig.reset == 'yes':
                rigSave = Myrig.objects.get(name=rig.name)
                rigSave.statustime = None
                rigSave.resettime = datetime.now(tz=pytz.timezone(timeZone))
                rigSave.resetcounter = rig.resetcounter + 1
                rigSave.save()
                print datetime.now(tz=pytz.timezone(timeZone)).strftime('[%m-%d-%Y %H:%M:%S]: ') + str(rig.name) + ' is resetting & email sent. [Unreachable/Offline] [Reset Attempt #' + str(rigSave.resetcounter) + ']'
                return None, True, True
            elif rig.email == 'yes' and rig.reset == 'no':
                rigSave = Myrig.objects.get(name=rig.name)
                rigSave.statustime = None
                rigSave.resettime = datetime.now(tz=pytz.timezone(timeZone))
                rigSave.resetcounter = rig.resetcounter + 1
                rigSave.save()
                print datetime.now(tz=pytz.timezone(timeZone)).strftime('[%m-%d-%Y %H:%M:%S]: ') + str(rig.name) + ' is Unreachable/Offline & email sent. [Reset Attempt #' + str(rigSave.resetcounter) + ']'
                return None, True, False
            elif rig.email == 'no' and rig.reset == 'yes':
                rigSave = Myrig.objects.get(name=rig.name)
                rigSave.statustime = None
                rigSave.resettime = datetime.now(tz=pytz.timezone(timeZone))
                rigSave.resetcounter = rig.resetcounter + 1
                rigSave.save()
                print datetime.now(tz=pytz.timezone(timeZone)).strftime('[%m-%d-%Y %H:%M:%S]: ') + str(rig.name) + ' is resetting. [Unreachable/Offline] [Reset Attempt #' + str(rigSave.resetcounter) + ']'
                return None, False, True
            else:
                print datetime.now(tz=pytz.timezone(timeZone)).strftime('[%m-%d-%Y %H:%M:%S]: ') + 'unable to process reset, email or restart timers for ' + rig.name + '. [Err 1]'
                return None, None, None
        else:
            print datetime.now(tz=pytz.timezone(timeZone)).strftime('[%m-%d-%Y %H:%M:%S]: ') + str(rig.name) + ' continues to remain Unreachable/Offline.'
            return None, None, None

def result_two_three_gpu(rig, result):
    import pytz 
    from datetime import tzinfo, timedelta, datetime
    from pimon.scripts.utils import pretty_date
    from pimon.models import ConfigGlobal, Myrig
    timeZone = ConfigGlobal.objects.filter(pk=1)[0].timezone
    if rig.resettime == None:
        if rig.statustime == None:
            if result[1] == True and result[2] == True:
                if rig.resetcounter == 0:
                    return None, None, None
                else:
                    rigSave = Myrig.objects.get(name=rig.name)
                    rigSave.firststatus = None
                    rig.resetcounter = 0
                    return None, None, None
            elif result[1] == False and result[2] == False:
                rigSave = Myrig.objects.get(name=rig.name)
                if rig.resetcounter == 0:
                    rigSave.firststatus = datetime.now(tz=pytz.timezone(timeZone))
                rigSave.statustime = datetime.now(tz=pytz.timezone(timeZone))
                rigSave.save()
                print datetime.now(tz=pytz.timezone(timeZone)).strftime('[%m-%d-%Y %H:%M:%S]: ') + str(rig.name) + ' detected Low Hashrate & High Temp(s).'
                return None, None, None
            elif result[1] == False:
                rigSave = Myrig.objects.get(name=rig.name)
                if rig.resetcounter == 0:
                    rigSave.firststatus = datetime.now(tz=pytz.timezone(timeZone))
                rigSave.statustime = datetime.now(tz=pytz.timezone(timeZone))
                rigSave.save()
                print datetime.now(tz=pytz.timezone(timeZone)).strftime('[%m-%d-%Y %H:%M:%S]: ') + str(rig.name) + ' detected Low Hashrate.'
                return None, None, None
            elif result[2] == False:
                rigSave = Myrig.objects.get(name=rig.name)
                if rig.resetcounter == 0:
                    rigSave.firststatus = datetime.now(tz=pytz.timezone(timeZone))
                rigSave.statustime = datetime.now(tz=pytz.timezone(timeZone))
                rigSave.save()
                print datetime.now(tz=pytz.timezone(timeZone)).strftime('[%m-%d-%Y %H:%M:%S]: ') + str(rig.name) + ' detected High Temp(s).'
                return None, None, None
            else:
                print datetime.now(tz=pytz.timezone(timeZone)).strftime('[%m-%d-%Y %H:%M:%S]: ') + 'unable to detect result status for ' + rig.name + '. [Err 2]'
                return None, None, None
        else:
            if result[1] == False or result[2] == False:
                dTime = datetime.now(tz=pytz.timezone(timeZone)) - rig.statustime
                if dTime >= timedelta(minutes=ConfigGlobal.objects.filter(pk=1)[0].gpureset):
                    if rig.email == 'yes' and rig.reset == 'yes':
                        rigSave = Myrig.objects.get(name=rig.name)
                        rigSave.statustime = None
                        rigSave.resettime = datetime.now(tz=pytz.timezone(timeZone))
                        rigSave.resetcounter = rig.resetcounter + 1
                        rigSave.save()
                        print datetime.now(tz=pytz.timezone(timeZone)).strftime('[%m-%d-%Y %H:%M:%S]: ') + str(rig.name) + ' is resetting & email sent. [Low Hashrate or High Temps] [Reset Attempt #' + str(rigSave.resetcounter) + ']'
                        return None, True, True
                elif rig.email == 'yes' and rig.reset == 'no':
                    rigSave = Myrig.objects.get(name=rig.name)
                    rigSave.statustime = None
                    rigSave.resettime = datetime.now(tz=pytz.timezone(timeZone))
                    rigSave.resetcounter = rig.resetcounter + 1
                    rigSave.save()
                    # Add email function here
                    print datetime.now(tz=pytz.timezone(timeZone)).strftime('[%m-%d-%Y %H:%M:%S]: ') + str(rig.name) + ' encountered Low Hashrate or High Temps & email sent. [Reset Attempt #' + str(rigSave.resetcounter) + ']'
                    return None, True, False
                elif rig.email == 'no' and rig.reset == 'yes':
                    rigSave = Myrig.objects.get(name=rig.name)
                    rigSave.statustime = None
                    rigSave.resettime = datetime.now(tz=pytz.timezone(timeZone))
                    rigSave.resetcounter = rig.resetcounter + 1
                    rigSave.save()
                    print datetime.now(tz=pytz.timezone(timeZone)).strftime('[%m-%d-%Y %H:%M:%S]: ') + str(rig.name) + ' is resetting. [Low Hashrate or High Temps] [Reset Attempt #' + str(rigSave.resetcounter) + ']'
                    return None, False, True
                else:
                    if result[1] == False and result[2] == False:
                        print datetime.now(tz=pytz.timezone(timeZone)).strftime('[%m-%d-%Y %H:%M:%S]: ') + str(rig.name) + ' continues to experience Low Hashrate & High Temp(s).'
                        return None, None, None
                    elif result[1] == False:
                        print datetime.now(tz=pytz.timezone(timeZone)).strftime('[%m-%d-%Y %H:%M:%S]: ') + str(rig.name) + ' continues to experience Low Hashrate.'
                        return None, None, None
                    elif result[2] == False:
                        print datetime.now(tz=pytz.timezone(timeZone)).strftime('[%m-%d-%Y %H:%M:%S]: ') + str(rig.name) + ' continues to experience High Temp(s).'
                        return None, None, None
                    else:
                        print datetime.now(tz=pytz.timezone(timeZone)).strftime('[%m-%d-%Y %H:%M:%S]: ') + 'unable to detect status result for ' + rig.name + '. [Err 3]'
                        return None, None, None
            else:
                rigSave = Myrig.objects.get(name=rig.name)
                rigSave.statustime = None
                rigSave.firststatus = None
                rigSave.save()
                print datetime.now(tz=pytz.timezone(timeZone)).strftime('[%m-%d-%Y %H:%M:%S]: ') + str(rig.name) + ' is now stable.'
                return None, None, None
    else:
        if result[1] == True and result[2] == True:
                rigSave = Myrig.objects.get(name=rig.name)
                rigSave.resettime = None
                rigSave.firststatus = None
                rigSave.resetcounter = 0
                rigSave.save()
                print datetime.now(tz=pytz.timezone(timeZone)).strftime('[%m-%d-%Y %H:%M:%S]: ') + str(rig.name) + ' is now online after reset.'
                return None, None, None
        else:
            if rig.resetcounter < ConfigGlobal.objects.filter(pk=1)[0].gpuresetattempts:
                rigSave = Myrig.objects.get(name=rig.name)
                rigSave.resettime = None
                rigSave.save()
                print datetime.now(tz=pytz.timezone(timeZone)).strftime('[%m-%d-%Y %H:%M:%S]: ') + str(rig.name) + ' is now online after reset but encountering Low Hash/High Temps. Resetting Timers.'
                return None, None, None
            else:
                print datetime.now(tz=pytz.timezone(timeZone)).strftime('[%m-%d-%Y %H:%M:%S]: ') + 'The rig ' + str(rig.name) + ' has been reset ' + str(rig.resetcounter) + ' times and continues to have Low Hashrate and/or High Temp(s) issues since ' + str(pretty_date(rig.firststatus)) + str(rig.firststatus.strftime(' [%m-%d-%Y %H:%M:%S]')) + '.'
                return None, None, None
