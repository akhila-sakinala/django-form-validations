from django import forms
from django.core import validators

def check_name(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("Name need to start with Z")

class FormData(forms.Form):
    name = forms.CharField(validators=[validators.MaxLengthValidator(5),check_name])
    email = forms.EmailField()
    verify_email = forms.EmailField(label="This field is required")
    
    def clean(self):
        all_clean_data  = super(FormData,self).clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Emails do not match!")
        

