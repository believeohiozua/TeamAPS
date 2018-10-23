from django import forms
from .models import userProfile
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from .models import profile
class contactForm(forms.Form):
	name = forms.CharField(required = False, max_length=20, help_text = '')
	email = forms.EmailField(required = True)
	comment = forms.CharField(required = True, widget = forms.Textarea) 
	
	
	
NETWORK_CHOICE= [
    ('mtn', 'MTN'),
    ('glo', 'GLO'),
    ('airtel', 'AIRTEL'),
    ('9mobile', '9MOBILE'),
	('visafone', 'VISAFONE'),
    ]
RECHARGE_CHOICE= [
    ('airtime', 'AIRTIME'),
    ('data', 'DATA'),
	('recharge_wallet', 'APS WALLET'),
    ]
BANK_CHOICE= [
    ('Access Bank Plc', 'Access Bank Plc' ),
	('Diamond Bank Plc', 'Diamond Bank Plc'),
	('Fidelity Bank Plc', 'Fidelity Bank Plc'),
	('First City Monument Bank Plc', 'First City Monument Bank Plc'),
	('First Bank of Nigeria Limited', 'First Bank of Nigeria Limited'),
	('Guaranty Trust Bank Plc', 'Guaranty Trust Bank Plc'),
	('Union Bank of Nigeria Plc', 'Union Bank of Nigeria Plc',),
	('United Bank for Africa Plc', 'United Bank for Africa Plc'),
	('Zenith Bank Plc', 'Zenith Bank Plc'),
	('Citi Bank Nigeria Limited', 'Citi Bank Nigeria Limited'),
	('Ecobank Nigeria Plc', 'Ecobank Nigeria Plc'),
	('Heritage Banking Company Limited', 'Heritage Banking Company Limited'),
	('Keystone Bank Limited', 'Keystone Bank Limited'),
	('Polaris Bank Limited', 'Polaris Bank Limited'),
	('Stanbic IBTC Bank Plc', 'Stanbic IBTC Bank Plc'),
	('Standard Chartered', 'Standard Chartered'),
	('Sterling Bank Plc', 'Sterling Bank Plc'),
	('Unity Bank Plc', 'Unity Bank Plc'),
	('Wema Bank Plc', 'Wema Bank Plc'),
    ]
class depositForm(forms.Form):
	network_select = forms.CharField(required = True, label='Select Network', widget=forms.Select(choices=NETWORK_CHOICE))
	Amount = forms.IntegerField(required = True, min_value = 50, max_value = 50000, help_text = '')
	Voucher_Pin = forms.IntegerField(required = True, help_text = 'enter recharge card pin')
	Voucher_serial_number = forms.IntegerField(required = True, help_text = 'Enter recharge serial number')
	select_bank = forms.CharField(required = True, label='select bank?', widget=forms.Select(choices=BANK_CHOICE))
	bank_account_name = forms.CharField(required = True, max_length=20, help_text = "enter benefitiary's name")
	bank_account_number = forms.CharField(required = True, max_length=20, help_text = "enter benefitiary's bank account number")
	phone_number= forms.IntegerField(required = True, help_text = 'Enter Phone Number')
	depositor_name = forms.CharField(required = False, max_length=20, help_text = "Depositor's name")
	
	
class purchaseForm(forms.Form):
	Recharge = forms.CharField(required = True, label='recharge?', widget=forms.Select(choices=RECHARGE_CHOICE))
	Amount = forms.IntegerField(required = True,  help_text = 'enter recharge amount Note you can recharge as small as 50NGN and as much as 50,000NGN')
	network_select = forms.CharField(required = True, label='select network?', widget=forms.Select(choices=NETWORK_CHOICE))
	phone_number= forms.IntegerField(required = True, help_text = 'Enter Phone Number') 
	
	
class profileForm(forms.Form):
	#Profile_picture = forms.ImageField()
	Name = forms.CharField(required = True, max_length=50, label= 'Full Names')
	Address = forms.EmailField(required = True)
	phone_number =  forms.IntegerField(required = True)


class UploadFile(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.ImageField()


from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )

		
		
		


from django.contrib.auth.forms import UserCreationForm

class MyRegistrationForm(UserCreationForm):
    extra_field = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username", "extra_field", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.extra_field = self.cleaned_data["extra_field"]
        if commit:
            user.save()
        return user

