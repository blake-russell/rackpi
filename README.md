# rackpi
Monitor/Reset GPU Mining Rig via a Raspberry Pi Zero (or other iterations of RPi)

## Create your secrets.py
Create a "secrets.py" under pimon an include app's secret key, allowed_hosts, and email settings...

```
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '<SECRET_KEY_GENERATED_BY_DJANGO>'

# IP addresses that will listen for requests
ALLOWED_HOSTS = ['localhost','127.0.0.1']

# Email Settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'yourgmailaddress@gmail.com'
EMAIL_HOST_PASSWORD = 'silly four letr pass'
EMAIL_PORT = 587
```

## Startup
Illicit the migrate manage.py to create your database. 

Make sure you have created a superuser as well, you will use that to login to the application.

## GPIO Layout
You will need a multi-channel DC 5V relay module. I used an 'ELEGOO 8 Channel DC 5V Relay Module with Optocoupler'

Below is the layout that I used in my personal application so that it can be reference in the add/edit rig modules.

 GPIO # | Relay #
------------ | -------------
26 | 01
19 | 02
13 | 03
06 | 04
05 | 05
21 | 06
20 | 07
16 | 08
