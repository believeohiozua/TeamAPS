from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import contactForm
from .forms import depositForm
from .forms import purchaseForm
from .models import userProfile
from .forms import profileForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save

# Create your views here.
def FAQs(request):
	
	context = {'FAQs':FAQs,}
	template = 'FAQs.html'
	return render(request, template, context)
	
	
def contact(request):
	title = 'CONTACT US'
	form = contactForm(request.POST or None)
	confirm_message = " we are eager to hear from you! Speak with someone from APS CONTACT US For all account, deposit, withdrawal, developer And business enquiries"
	
	
	if form.is_valid():
		name = form.cleaned_data['name']
		comment = form.cleaned_data['comment']
		subject = 'message from APSite.com'
		message = '%s %s' %(comment, name)
		emailFrom = form.cleaned_data['email']
		emailTo = [settings.EMAIL_HOST_USER]
		send_mail(subject,message, emailFrom,emailTo,  fail_silently = True),
		title = "THANKS"
		confirm_message = "thanks for reaching out to use the APS team will get back to you shortly"
		form = None
	context = {'form':form, 'title': title, 'confirm_message': confirm_message,}
	template = 'contact.html'
	return render(request, template, context)
	
	
	
def deposit(request):
	title = 'DEPOSIT SLIP'
	form = depositForm(request.POST or None)
	confirm_message = None
	
	
	if form.is_valid():
		network_select = form.cleaned_data['network_select']
		Amount = form.cleaned_data['Amount']
		Voucher_Pin = form.cleaned_data['Voucher_Pin']
		Voucher_serial_number =form.cleaned_data['Voucher_serial_number']
		select_bank = form.cleaned_data['select_bank']
		bank_account_name = form.cleaned_data['bank_account_name']
		bank_account_number = form.cleaned_data['bank_account_number']
		phone_number = form.cleaned_data['phone_number']
		depositor_name = form.cleaned_data['depositor_name']
		
		subject = 'APS DEPOSIT ALERT'
		message = (network_select, Amount, Voucher_Pin, select_bank, bank_account_number, phone_number ,depositor_name, Voucher_serial_number)
		emailFrom = form.cleaned_data['depositor_name']
		emailTo = [settings.EMAIL_HOST_USER]
		send_mail(subject, message, emailFrom,emailTo,  fail_silently = True),
		title = "REQUEST SENT"
		confirm_message = "thanks! your deposit shall be processed shortly. if confirmed, your account will be credited"
		form = None
	context = {'form':form, 'title': title, 'confirm_message': confirm_message,}
	template = 'deposit.html'
	return render(request, template, context)
	
	
	
def purchase(request):
	title = 'PURCHASE SLIP'
	form = purchaseForm(request.POST or None)
	confirm_message = None
	
	
	if form.is_valid():
		Recharge = form.cleaned_data['Recharge']
		Amount = form.cleaned_data['Amount']
		network_select = form.cleaned_data['network_select']
		phone_number = form.cleaned_data['phone_number']
		
		subject = 'APS PURCHASE ALERT'
		message = (Recharge, Amount, network_select, phone_number)
		emailFrom = form.cleaned_data['phone_number']
		emailTo = [settings.EMAIL_HOST_USER]
		send_mail(subject,message, emailFrom,emailTo,  fail_silently = True),
		title = "SUCCESSFULLY"
		confirm_message = "THANKS FOR YOUR PATRONAGE!"
		form = None
	context = {'form':form, 'title': title, 'confirm_message': confirm_message,}
	template = 'purchase.html'
	return render(request, template, context)


def profileView(request):
	user = request.user
	context = {'user': user}
	template = 'profileview.html'
	return render(request, template, context)

from django.shortcuts import redirect	
from .forms import	DocumentForm
	
def profile_form(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            
            
            form.save()
            return redirect('profileview')
    else:
        form = DocumentForm()
    return render(request, 'profile.html', {
        'form': form
    })
	
	
	
	
from .forms import MyRegistrationForm

def register_user(request):
	if request == 'POST':
		form = MyRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect ('accounts/login/')
			
	args = {}
	args.update(csrf(request))
	
	args['form'] = MyRegistrationForm()
	
	#return render_to_response('signup.html', args)
	context = {'form':form}
	template = 'signup.html'
	return render(request, template, context)
	