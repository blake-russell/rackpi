from __future__ import unicode_literals
from django.utils.translation import gettext as _
from multiselectfield import MultiSelectField
from django.db import models
from django.utils import timezone
from scripts.choices import *
from scripts.timezones import *

# Create your models here.

class Miner(models.Model):
    class Meta:
        ordering = ['name']
    name = models.CharField(max_length=30, unique=True)
    type = models.CharField(choices=MINER_TYPE, max_length=17)
    algo = models.CharField(choices=MINER_ALG, max_length=30)
    hash = models.FloatField(default="0.0")
    power = models.FloatField(default="0.0")
    price = models.FloatField(default="0.0")
    software = models.CharField(choices=MINER_SOFTWARE, max_length=15)
    port = models.IntegerField()
    def __str__(self):
        return self.name

class Myrig(models.Model):
    class Meta:
        ordering = ['name']
    name = models.CharField(max_length=100, unique=True)
    miner = models.ForeignKey(Miner, on_delete=models.CASCADE, related_name="myrigminer")
    algo = models.CharField(choices=MINER_ALG, max_length=17, default="Any")
    hash = models.FloatField(default="0.0")
    power = models.FloatField(default="0.0")
    price = models.FloatField(default="0.0")
    monitor = models.CharField(choices=YES_OR_NO, max_length=3, default=NO)
    monitoremail = models.CharField(choices=YES_OR_NO, max_length=3, default=YES)
    address = models.GenericIPAddressField(default="0.0.0.0")
    port = models.IntegerField(default=0)
    software = models.CharField(choices=MINER_SOFTWARE, max_length=15, default=NONE)
    user = models.CharField(max_length=100, default="user")
    passw = models.CharField(max_length=100, default="pass")
    reset = models.CharField(choices=YES_OR_NO, max_length=3, default=NO)
    gpio = models.IntegerField(choices=GPIO_PIN, default=-1)
    temp = models.FloatField(default="0.0")
    hashr = models.FloatField(default="0.0")
    email = models.CharField(choices=YES_OR_NO, max_length=3, default=YES)
    status = models.CharField(choices=ONLINE_OR_OFFLINE, max_length=7, default=ONLINE)
    statustime = models.DateTimeField(blank=True, null=True)
    resettime = models.DateTimeField(blank=True, null=True)
    resetcounter = models.IntegerField(default=0)
    firststatus = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.name

class ConfigGlobal(models.Model):
    sitename = models.CharField(max_length=100, default='Pimon')
    timezone = models.CharField(choices=TIME_ZONES, max_length=100, default='US/Central')
    electriccost = models.FloatField(default="10.1")
    emailtype = models.CharField(choices=EMAIL_TYPE, max_length=20, default=GMAIL)
    email = models.EmailField(max_length=200, blank=True)
    emailpass = models.CharField(max_length=200, blank=True)
    emailsendto = models.EmailField(blank=True)
    module = MultiSelectField(choices=LOAD_MODULE, blank=True)
    wtmincludemyrigs = models.CharField(choices=YES_OR_NO, max_length=3, default=YES)
    gpurefresh = models.IntegerField(default=30)
    gpucheck = models.FloatField(default=1)
    gpureset = models.FloatField(default=5)
    gpuresetwait = models.FloatField(default=5)
    gpuresetattempts = models.FloatField(default=3)
    asicrefresh = models.IntegerField(default=30)
    asiccheck = models.FloatField(default=1)
    asicreset = models.FloatField(default=5)
    asicresetwait = models.FloatField(default=5)
    asicresetattempts = models.FloatField(default=3)
    pdurefresh = models.IntegerField(default=1)
    temprefresh = models.IntegerField(default=1)
    forecastrefresh = models.IntegerField(default=60)
    walletrefresh = models.IntegerField(default=60)
    poolrefresh = models.IntegerField(default=30)
    profitrefresh = models.IntegerField(default=60)
    wtmrefresh = models.IntegerField(default=60)
    iframefresh = models.IntegerField(default=0)
    autosetup = models.IntegerField(default=0)
    def __str__(self):
        return self.sitename

class ConfigPool(models.Model):
    class Meta:
        ordering = ['name']
    name = models.CharField(max_length=100, unique=True)
    baseurl = models.CharField(max_length=200, blank=True)
    midurl = models.CharField(max_length=200, blank=True)
    tailurl = models.CharField(max_length=200, blank=True)
    viewurl1 = models.CharField(max_length=200, blank=True)
    viewurl2 = models.CharField(max_length=200, blank=True)
    dashboardurl1 = models.CharField(max_length=200, blank=True)
    dashboardurl2 = models.CharField(max_length=200, blank=True)
    balanceurl1 = models.CharField(max_length=200, blank=True)
    balanceurl2 = models.CharField(max_length=200, blank=True)
    autoswurl = models.CharField(max_length=200, blank=True)
    autosw = models.CharField(max_length=200, blank=True)
    confirmed = models.CharField(max_length=200, blank=True)
    last24hr = models.CharField(max_length=200, blank=True)
    poolhash = models.CharField(max_length=200, blank=True)
    nethash = models.CharField(max_length=200, blank=True)
    price = models.CharField(max_length=200, blank=True)
    autosw = models.CharField(max_length=200, blank=True)
    autoswuse = models.CharField(choices=YES_OR_NO, max_length=3, default=NO)
    def __str__(self):
        return self.name

class Coin(models.Model):
    class Meta:
        ordering = ['name']
    abv = models.CharField(max_length=100)
    name = models.CharField(max_length=100, unique=True)
    wtm = models.IntegerField(default=0)
    cmc = models.IntegerField(default=0)
    polo = models.CharField(max_length=100,default="0")
    grav = models.CharField(max_length=100,default="0")
    cbri = models.IntegerField(default=0)
    algo = models.CharField(choices=MINER_ALG, max_length=20, default="None")
    decimal = models.IntegerField(default="2")
    enable = models.CharField(choices=YES_OR_NO, max_length=3, default=YES)
    def __str__(self):
        return self.name

class ConfigTicker(models.Model):
    class Meta:
        ordering = ['coin']  
    coin = models.OneToOneField(Coin)
    def __str__(self):
        return self.coin.name

class Mypool(models.Model):
    class Meta:
        ordering = ['name']
    name = models.CharField(max_length=100, unique=True)        
    pool = models.ForeignKey(ConfigPool, on_delete=models.CASCADE, related_name="mypoolpool")
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE, related_name="poolcoin")
    followsw = models.CharField(choices=YES_OR_NO, max_length=3, default=NO)
    api = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    suprid = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.name

class Mypdu(models.Model):
    class Meta:
        ordering = ['name']
    name = models.CharField(max_length=100, unique=True)  
    pdutype = models.CharField(choices=PDU_TYPE, max_length=30, default="HP_S124") 
    address = models.GenericIPAddressField(default="0.0.0.0")
    calltype = models.CharField(choices=PDU_TYPE, max_length=30, default="SNMPv2c")
    smtpcommunity = models.CharField(max_length=200)
    smtppassword = models.CharField(max_length=200)
    smtpport = models.IntegerField()
    bank1watt = models.CharField(max_length=200)
    bank1amp = models.CharField(max_length=200)
    bank1volt = models.CharField(max_length=200)
    bank2watt = models.CharField(max_length=200)
    bank2amp = models.CharField(max_length=200)
    bank2volt = models.CharField(max_length=200)
    bank3watt = models.CharField(max_length=200)
    bank3amp = models.CharField(max_length=200)
    bank3volt = models.CharField(max_length=200)
    bank4watt = models.CharField(max_length=200)
    bank4amp = models.CharField(max_length=200)
    bank4volt = models.CharField(max_length=200)
    bank5watt = models.CharField(max_length=200)
    bank5amp = models.CharField(max_length=200)
    bank5volt = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class ConfigTemp(models.Model):
    reading = models.CharField(choices=TEMP_READING, max_length=10, default="Fahrenheit")
    model = models.CharField(choices=TEMP_MODEL, max_length=10, default="DHT22")
    gpio = models.IntegerField(choices=GPIO_PIN, default=-1)
    def __str__(self):
        return self.model

class ConfigForecast(models.Model):
    reading = models.CharField(choices=FORECAST_SITE, max_length=30, default="None")
    api = models.CharField(max_length=100, blank=True)
    zipcode = models.IntegerField(blank=True)

class ConfigWtm(models.Model):
    algo = models.CharField(choices=MINER_ALG, max_length=30)
    customhash = models.FloatField(default="0.0")
    custompower = models.FloatField(default="0.0")
    customprice = models.FloatField(default="0.0")
    def __str__(self):
        return self.algo

class ConfigWallet(models.Model):
    class Meta:
        ordering = ['name']
    name = models.CharField(max_length=100, unique=True)
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE, related_name="walletcoin")
    address = models.CharField(max_length=200)
    balance = models.FloatField(default="0.0") 
    def __str__(self):
        return self.name