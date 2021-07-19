from django.shortcuts import render, get_object_or_404, render_to_response
from django.shortcuts import redirect
from django.http import JsonResponse
from django import forms
from pimon.models import *
from scripts.utils import *
from pimon import settings
from choices import *
from .forms import *
import time

# Create your views here.

def home(request):
	config = ConfigGlobal.objects.filter(pk=1).get()
	return render(request, 'pimon/home.html', {'config': config})

def returnfeedback(request, id):
	if id == '0':
		feedback = 'Your request could not be processed or located.'
		color = 'red'
	elif id == '1':
		feedback = 'Please select an option.'
		color = ''
	elif id == '2':
		feedback = 'Your request was processed successfully.'
		color = 'green'
	elif id == '3':
		feedback = 'Config saved successfully.'
		color = 'green'
	elif id == '4':
		feedback = 'Config failed to save.'
		color = 'red'
	else:
		feedback = ''
		color = ''
	return render(request, 'pimon/returnfeedback.html', {'feedback': feedback, 'color': color})

def myrigs(request):
	myrigs = Myrig.objects.all()
	config = ConfigGlobal.objects.filter(pk=1).get()
	return render(request, 'pimon/myrigs.html', {'rig': myrigs, 'config': config})

def addrig(request):
	config = ConfigGlobal.objects.filter(pk=1).get()
	if request.method == 'POST':
		form = MyrigForm(request.POST)
		if form.is_valid():
			rig = form.save(commit=False)
			minerFK = request.POST['miner']
			if minerFK == '13' or minerFK == '14':
				rig.save()
			else:
				minerObj = Miner.objects.filter(pk=minerFK).get()
				rig.algo = minerObj.algo
				rig.hash = minerObj.hash
				rig.power = minerObj.power
				rig.price = minerObj.price
				rig.port = minerObj.port
				rig.software = minerObj.software
				rig.save()
			return redirect('myrigs')
	else:
		form = MyrigForm()
	return render(request, 'pimon/addrig.html', {'form': form, 'config': config})

def editrig(request, pk):
	config = ConfigGlobal.objects.filter(pk=1).get()
	rig = get_object_or_404(Myrig, pk=pk)
	if request.method == 'POST':
		form = MyrigForm(request.POST, instance=rig)
		if form.is_valid():
			rig = form.save(commit=False)
			rig.save()
			return redirect('myrigs')
	else:
		form = MyrigForm(instance=rig)
	return render(request, 'pimon/editrig.html', {'form': form, 'config': config})

def delrig(request, pk):
	Myrig.objects.filter(pk=pk).delete()
	return redirect('myrigs')

def confighome(request):
	config = ConfigGlobal.objects.filter(pk=1).get()
	return render(request, 'pimon/confighome.html', {'config': config})

def configglobal(request):
	config = get_object_or_404(ConfigGlobal, pk=1)
	if request.method == 'POST':
		form = ConfigGlobalForm(request.POST, instance=config)
		if form.is_valid():
			config = form.save(commit=False)
			config.save()
			return redirect('returnfeedback', id=3)
	else:
		form = ConfigGlobalForm(instance=config)
	return render(request, 'pimon/configglobal.html', {'form': form})