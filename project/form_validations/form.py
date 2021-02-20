from django import forms

class FormData(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    