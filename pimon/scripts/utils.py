
def send_reset_mail(rigs):
    from django.core.mail import send_mail
    from pimon.models import ConfigGlobal
    if len(rigs) > 0:
        if ConfigGlobal.objects.filter(pk=1)[0].emailsendto != None:
            sendto = ConfigGlobal.objects.filter(pk=1)[0].email
        if len(rigs) > 1:
            message = 'Your monitoring device ' + str(ConfigGlobal.objects.filter(pk=1)[0].sitename) + ' has reset the following devices: \n\n'
            message2 = ''
            subject = str(ConfigGlobal.objects.filter(pk=1)[0].sitename) + ' Reset Notification'
            for rig in rigs:
                if rig.reset == 'yes':
                    message = message + ' - ' + rig.name + ': ' + rig.address + '\n'
                else:
                    if message2 == '':
                        message2 = '\nDevices not reset but encountering problems: \n\n' + ' - ' + rig.name + ': ' + rig.address + '\n'
                    else:
                        message2 = message2 + ' - ' + rig.name + ': ' + rig.address + '\n'
            send_mail(
                subject,
                message + message2,
                ConfigGlobal.objects.filter(pk=1)[0].email,
                [sendto],
                fail_silently=False,
                )
        else:
            if rigs[0].reset == 'yes':
                message = 'Your monitoring device ' + str(ConfigGlobal.objects.filter(pk=1)[0].sitename) + ' has reset the following device: \n\n - ' + rigs[0].name + ': ' + rigs[0].address
            else:
                message = 'Your monitoring device ' + str(ConfigGlobal.objects.filter(pk=1)[0].sitename) + ' has detected problems on the following device: \n\n - ' + rigs[0].name + ': ' + rigs[0].address
            subject = str(ConfigGlobal.objects.filter(pk=1)[0].sitename) + ' Reset Notification'
            send_mail(
                subject,
                message,
                ConfigGlobal.objects.filter(pk=1)[0].email,
                [sendto],
                fail_silently=False,
                )
    else:
        pass

def print_http_response(f):
    """ Wraps a python function that prints to the console, and
    returns those results as a HttpResponse (HTML)"""

    from django.http import HttpResponse
    import sys

    class WritableObject:
        def __init__(self):
            self.content = []
        def write(self, string):
            self.content.append(string)

    def new_f(*args, **kwargs):
        printed = WritableObject()
        sys.stdout = printed
        f(*args, **kwargs)
        sys.stdout = sys.__stdout__
        return HttpResponse(['<BR>' if c == '\n' else c for c in printed.content ])
    return new_f

def pretty_date(time=False):
    """
    Get a datetime object or a int() Epoch timestamp and return a
    pretty string like 'an hour ago', 'Yesterday', '3 months ago',
    'just now', etc
    """
    from datetime import tzinfo, timedelta, datetime
    from pimon.models import ConfigGlobal
    import pytz
    
    timeZone = ConfigGlobal.objects.filter(pk=1)[0].timezone

    now = datetime.now(tz=pytz.timezone(timeZone))
    if type(time) is int:
        diff = now - datetime.fromtimestamp(time)
    elif isinstance(time,datetime):
        diff = now - time
    elif not time:
        diff = now - now
    second_diff = diff.seconds
    day_diff = diff.days

    if day_diff < 0:
        return ''

    if day_diff == 0:
        if second_diff < 10:
            return "under 10 seconds ago"
        if second_diff < 60:
            return str(second_diff) + " seconds ago"
        if second_diff < 120:
            return "a minute ago"
        if second_diff < 3600:
            return str(second_diff / 60) + " minutes ago"
        if second_diff < 7200:
            return "an hour ago"
        if second_diff < 86400:
            return str(second_diff / 3600) + " hours ago"
    if day_diff == 1:
        return "Yesterday"
    if day_diff < 7:
        return str(day_diff) + " day(s) ago"
    if day_diff < 31:
        return str(day_diff / 7) + " week(s) ago"
    if day_diff < 365:
        return str(day_diff / 30) + " month(s) ago"
    return str(day_diff / 365) + " year(s) ago"