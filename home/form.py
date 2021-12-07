from django import forms
from .models import Contact
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message')

    def clean_email(self):
        domain_list = ["gmail.com", ]
        email = self.cleaned_data['email']
        domain = email.split('@')
        domain = domain[1]

        if domain in domain_list:
            raise ValidationError("please put a professional email address")

        return email