"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
from django.urls import path, include

User.add_to_class('is_verified', models.BooleanField(default=True))


from django_otp.admin import OTPAdminSite

class MyOTPAdminSite(OTPAdminSite):
    def has_permission(self, request):
        return request.user.is_active and request.user.is_verified

admin.site.__class__ = MyOTPAdminSite


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('newsapi.api.urls')),

]
