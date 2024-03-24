# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 22:48:52 2024

@author: gentleH
"""

from django import forms
from .models import Topic,Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic 
        fields = ['text']
        labels = {'text':''}
        
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry 
        fields = ['text']
        lables = {'text':''}
        widgets = {'text':forms.Textarea(attrs={'cols':80})}