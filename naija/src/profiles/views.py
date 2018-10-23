from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
def home (request):
	context = {}
	template = 'home.html'
	return render(request, template, context)
	
	
	
def about(request):
	context = {}
	template = 'about.html'
	return render(request, template, context)
	
	
	

	
	
def deposit(request):
	context = locals()
	template = 'deposit.html'
	return render(request, template, context)
	

def purchase(request):
	context = locals()
	template = 'purchase.html'
	return render(request, template, context)
	
	
@login_required(login_url='/accounts/login/')
def userProfile(request):
	user = request.user 
	context = {'user': user}
	template = 'profile.html'
	return render(request, template, context)