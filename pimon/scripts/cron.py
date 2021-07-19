from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Q
from datetime import tzinfo, timedelta, datetime
from django_cron import CronJobBase, Schedule
from pimon.models import ConfigGlobal, Myrig
from .checkgpu import *
from .checkasic import *
from .utils import send_reset_mail
import RPi.GPIO as GPIO
import time
import pytz

class CheckGPU(CronJobBase):
    """
    #Check Monitored GPU's enabled in MyRigs
    #Also responsible for monitoring custom FPGA cards/rigs in MyRigs
    """
    RUN_EVERY_MINS = ConfigGlobal.objects.filter(pk=1)[0].gpucheck if settings.DEBUG else 360   # 6 hours when not DEBUG
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'scripts.cron.CheckGPU'

    def do(self):
        emailList = []
        resetList = []
        timeZone = ConfigGlobal.objects.filter(pk=1)[0].timezone
        for rig in Myrig.objects.filter(Q(miner__type__contains='GPU') | Q(miner__type__contains='cFPGA'), status='Online'):
            if rig.monitoremail == 'yes' or rig.reset == 'yes':
                result = check_gpu(rig)
                if result[0] == False:
                    gpuReturn = result_zero_gpu(rig)
                    if gpuReturn[1] == True and gpuReturn[2] == True:
                        if ConfigGlobal.objects.filter(pk=1)[0].email == '' or ConfigGlobal.objects.filter(pk=1)[0].emailpass == '':
                            print datetime.now(tz=pytz.timezone(timeZone)).strftime('[%m-%d-%Y %H:%M:%S]: ') + str(rig.name) + ' Email and/or Email Password are not setup in Global Configuration. Please do so to utilize Myrig Email features.' 
                            if rig.gpio == -1:
                                print datetime.now(tz=pytz.timezone(timeZone)).strftime('[%m-%d-%Y %H:%M:%S]: ') + str(rig.name) + ' GPIO number needs to be set under Myrig for the reset function to work properly.' 
                            else:
                                resetList.append(rig)
                        elif rig.gpio == -1:
                                emailList.append(rig)
                                print datetime.now(tz=pytz.timezone(timeZone)).strftime('[%m-%d-%Y %H:%M:%S]: ') + str(rig.name) + ' GPIO number needs to be set under Myrig for the reset function to work properly.' 
                        else:
                            emailList.append(rig)
                            resetList.append(rig)
                    elif gpuReturn[1] == True and gpuReturn[2] == False:
                        if ConfigGlobal.objects.filter(pk=1)[0].email == '' or ConfigGlobal.objects.filter(pk=1)[0].emailpass == '':
                            print datetime.now(tz=pytz.timezone(timeZone)).strftime('[%m-%d-%Y %H:%M:%S]: ') + str(rig.name) + ' Email and/or Email Password are not setup in Global Configuration. Please do so to utilize Myrig Email features.' 
                        else:
                            emailList.append(rig)
                    elif gpuReturn[1] == False and gpuReturn[2] == True:
                        if rig.gpio == -1:
                            print datetime.now(tz=pytz.timezone(timeZone)).strftime('[%m-%d-%Y %H:%M:%S]: ') + str(rig.name) + ' GPIO number needs to be set under Myrig for the reset function to work properly.' 
                        else:
                            resetList.append(rig)
                    else:
                        pass
                elif result[0] == True:
                    gpuReturn = result_two_three_gpu(rig, result)
                    if gpuReturn[1] == True and gpuReturn[2] == True:
                        if ConfigGlobal.objects.filter(pk=1)[0].email == '' or ConfigGlobal.objects.filter(pk=1)[0].emailpass == '':
                            print datetime.now(tz=pytz.timezone(timeZone)).strftime('[%m-%d-%Y %H:%M:%S]: ') + str(rig.name) + ' Email and/or Email Password are not setup in Global Configuration. Please do so to utilize Myrig Email features.' 
                            if rig.gpio == -1:
                                print datetime.now(tz=pytz.timezone(timeZone)).strftime('[%m-%d-%Y %H:%M:%S]: ') + str(rig.name) + ' GPIO number needs to be set under Myrig for the reset function to work properly.' 
                            else:
                                resetList.append(rig)
                        elif rig.gpio == -1:
                                emailList.append(rig)
                                print datetime.now(tz=pytz.timezone(timeZone)).strftime('[%m-%d-%Y %H:%M:%S]: ') + str(rig.name) + ' GPIO number needs to be set under Myrig for the reset function to work properly.' 
                        else:
                            emailList.append(rig)
                            resetList.append(rig)
                    elif gpuReturn[1] == True and gpuReturn[2] == False:
                        if ConfigGlobal.objects.filter(pk=1)[0].email == '' or ConfigGlobal.objects.filter(pk=1)[0].emailpass == '':
                            print datetime.now(tz=pytz.timezone(timeZone)).strftime('[%m-%d-%Y %H:%M:%S]: ') + str(rig.name) + ' Email and/or Email Password are not setup in Global Configuration. Please do so to utilize Myrig Email features.' 
                        else:
                            emailList.append(rig)
                    elif gpuReturn[1] == False and gpuReturn[2] == True:
                        if rig.gpio == -1:
                            print datetime.now(tz=pytz.timezone(timeZone)).strftime('[%m-%d-%Y %H:%M:%S]: ') + str(rig.name) + ' GPIO number needs to be set under Myrig for the reset function to work properly.' 
                        else:
                            resetList.append(rig)
                    else:
                        pass
                else:
                    print result
            else:
                pass
        #Run Reset function
        for rig in resetList:
            reset_gpio(rig)
        #Run Email function
        send_reset_mail(emailList)

        


