# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from . import form

def index(request):
    return render(request, 'index.html')

def forms(request):
    forms_obj = form.FormData()
    # handling post data coming from UI
    if request.method == 'POST':
        forms_obj = form.FormData(request.POST)
        if forms_obj.is_valid():
            form_data = {
                'name': forms_obj.cleaned_data['name'],
                'email': forms_obj.cleaned_data['email']
            }
            return render(request, 'forms.html', {'form_obj':forms_obj, 'form_data':form_data})
    return render(request, 'forms.html', {'form_obj':forms_obj})



