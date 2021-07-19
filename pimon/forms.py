from django import forms
from django.utils.translation import gettext as _
from .models import *
from scripts.choices import *
from scripts.timezones import *

class MyrigForm(forms.ModelForm):
	class Meta:
		model = Myrig
		fields = ('name','miner','algo','hash','power','price','monitor','monitoremail',
				'address','port','software', 'user','passw','reset','gpio','temp','hashr',
				'email','status')
	name = forms.CharField()
	miner = forms.ModelChoiceField(queryset=Miner.objects.all())
	algo = forms.ChoiceField(label="Algorithm", choices=MINER_ALG)
	hash = forms.FloatField(label="Hashrate (H/s)", initial="0.0")
	power = forms.FloatField(label="Power (W)", initial="0.0")
	price = forms.FloatField(label="Price", initial="0.0")
	monitor = forms.ChoiceField(label="Monitor Miner?", choices=YES_OR_NO, initial=NO)
	monitoremail = forms.ChoiceField(label="Monitor Email?", choices=YES_OR_NO, initial=NO)
	address = forms.GenericIPAddressField(label="IP Address", initial="0.0.0.0")
	port = forms.CharField(label="API port", initial=0)
	software = forms.ChoiceField(label="Software", choices=MINER_SOFTWARE, initial=NONE)
	user = forms.CharField(label="Username", initial="root")
	passw = forms.CharField(label="Password", initial="admin", required=False)
	reset = forms.ChoiceField(label="Reset on Problem?", choices=YES_OR_NO, initial=NO)
	gpio = forms.ChoiceField(label="GPIO Pin (BCM)", choices=GPIO_PIN, initial=-1)
	temp = forms.FloatField(label="High Temp", initial="0.0")
	hashr = forms.FloatField(label="Low Hash", initial="0.0")
	email = forms.ChoiceField(label="Email on reset?", choices=YES_OR_NO, initial=NO)
	status = forms.ChoiceField(label="Miner Status", choices=ONLINE_OR_OFFLINE, initial=ONLINE)

class ConfigGlobalForm(forms.ModelForm):
	class Meta:
		model = ConfigGlobal
		fields = ('sitename', 'timezone', 'electriccost', 'emailtype', 'email', 'emailpass',
					'emailsendto', 'module', 'wtmincludemyrigs', 'gpurefresh', 'gpucheck', 'gpureset',
					'gpuresetwait', 'gpuresetattempts', 'asicrefresh', 'asiccheck', 'asicreset',
					'asicresetwait', 'asicresetattempts', 'pdurefresh', 'temprefresh', 'forecastrefresh',
					'walletrefresh', 'poolrefresh', 'profitrefresh', 'wtmrefresh', 'iframefresh')	
	sitename = forms.CharField(label="Site Name")
	timezone = forms.ChoiceField(label="Time Zone", choices=TIME_ZONES, required=False)
	electriccost = forms.FloatField(label="Electric Cost", required=False)
	emailtype = forms.ChoiceField(label="Email Type", choices=EMAIL_TYPE, required=False)
	email = forms.EmailField(label="Email", required=False)
	emailpass = forms.CharField(label="Email Password", required=False)
	emailsendto = forms.EmailField(label="Send Email to", required=False)
	#module = MultipleChoiceField(label="Modules to Load", widget=forms.CheckboxSelectMultiple, choices=LOAD_MODULE)
	wtmincludemyrigs = forms.ChoiceField(label="WTM Include Myrigs", choices=YES_OR_NO)
	gpurefresh = forms.IntegerField(label="GPU Monitor Refresh Interval")
	gpucheck = forms.FloatField(label="GPU Reset Check Interval")
	gpureset = forms.FloatField(label="GPU Reset Threshold")
	gpuresetwait = forms.FloatField(label="GPU Reset Wait Timer")
	gpuresetattempts = forms.FloatField(label="Times to attempt GPU reset")
	asicrefresh = forms.IntegerField(label="ASIC Monitor Refresh Interval")
	asiccheck = forms.FloatField(label="ASIC Reset Check Interval")
	asicreset = forms.FloatField(label="ASIC Reset Threshold")
	asicresetwait = forms.FloatField(label="ASIC Reset Wait Timer")
	asicresetattempts = forms.FloatField(label="Times to attempt ASIC reset")
	pdurefresh = forms.IntegerField(label="PDU Monitor Refresh Interval")
	temprefresh = forms.IntegerField(label="Temp Monitor Refresh Interval")
	forecastrefresh = forms.IntegerField(label="Forecast Monitor Refresh Interval")
	walletrefresh = forms.IntegerField(label="Wallet Monitor Refresh Interval")
	poolrefresh = forms.IntegerField(label="Pool Monitor Refresh Interval")
	profitrefresh = forms.IntegerField(label="Profit Monitor Refresh Interval")
	wtmrefresh = forms.IntegerField(label="WTM Monitor Refresh Interval")
	iframefresh = forms.IntegerField(label="iFrame Monitor Refresh Interval")