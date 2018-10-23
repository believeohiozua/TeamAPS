from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm

# Create your models here.
class userProfile(models.Model):
	user = models.OneToOneField(User, on_delete= models.SET_NULL, null=True )
	Address = models.CharField(null=False, max_length=1000, help_text = '')
	Name = models.CharField(null=True, max_length=50, )
	Address = models.EmailField(max_length=200)
	phone_number =  models.IntegerField(null=True)
	Profile_picture = models.ImageField(upload_to = 'profile_image')
	
	def __str__(self):
		return self.user.username
def create_profile(sender, **kwargs):
	if kwargs ['created']:
		user_profile = userProfile.object.create(user=kwargs['instance'])
		
post_save.connect(create_profile, sender = User)


# Create your models here.
class profile(models.Model):
	name = models.CharField(max_length=20)
	description = models.TextField(default= 'description default text')
	#Location = models.CharField(max_length=20, default = 'my location default', blank= True, null = True  )
	#job = models.CharField(max_length=20, null = True)
	image = models.ImageField() #run pip install pillow
	def __unicode__(self):
		return self.name
		
		
		
class ProfileForm(ModelForm):
    class Meta:
        model =  profile
        fields = ['name', 'description', 'image']
		
		
		
		

		
		
		
		
		
class Document(models.Model):
	user = models.OneToOneField(User, on_delete= models.SET_NULL, null=True )
	description = models.CharField(max_length=255, blank=True)
	document = models.ImageField(upload_to='static/img/uploads/')
	uploaded_at = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.user.username
"""
def create_profile (sender, **kwargs):
	if kwargs['create']:
		userProfile = Document.object.create(user = kwargs [instance])
	
post_save.connect(create_profile, sender=User)
"""
from .forms import MyRegistrationForm	
	