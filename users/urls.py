# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 11:54:22 2024

@author: gentleH
"""

from django.urls import path,include
from . import views

app_name = 'users'
urlpatterns = [
    path('',include('django.contrib.auth.urls')),
    path('register/',views.register,name = 'register'),
    ]