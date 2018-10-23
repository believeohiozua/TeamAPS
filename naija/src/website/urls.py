"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from profiles import views
from profiles import views as profiles_views
from contact import views as contact_views

from contact import views as FAQs
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
	path('', profiles_views.home, name='home'),
	path('deposit/', contact_views.deposit, name='deposit'),
	path('about/', profiles_views.about, name='about'),
	path('profile/', contact_views.profile_form, name='profile'),
	path('profileview/', contact_views.profileView, name='profileview'),
	path('purchase/', contact_views.purchase, name='purchase'),
	path('contact/', contact_views.contact, name='contact'),
	path('FAQs/', contact_views.FAQs, name='FAQs'),
	path('accounts/', include('allauth.urls')),
	
	path('accounts/', include('django.contrib.auth.urls')),
	
]#+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
"""
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
"""
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)






#Add URL maps to redirect the base URL to our application

urlpatterns += [

]

# Use static() to add url mapping to serve static files during development (only)




#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [

]
