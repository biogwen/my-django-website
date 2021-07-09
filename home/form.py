from django import forms
from .models import Contact
from django.core.exceptions import ValidationError


class PostForm(forms.Form):

    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email_address = forms.EmailField(max_length=150)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)

    def clean_email(self):
        domain_list = ["gmail.com", ]
        email = self.cleaned_data['email']
        domain = email.split('@')
        domain = domain[1]

        if domain in domain_list:
            raise ValidationError("please put a professional email address")

        return email