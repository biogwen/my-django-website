
from django import forms
from django.core.exceptions import ValidationError

from .models import Email, Quizz

class PostForm(forms.ModelForm):

    class Meta:
        model = Email
        fields = ('email',)

    def clean_email(self):
        domain_list = ["gmail.com", ]
        email = self.cleaned_data['email']
        domain = email.split('@')
        domain = domain[1]

        if domain in domain_list:
            raise ValidationError("please put a professional email address")

        return email
        
        
class quizagile(forms.ModelForm):
    class Meta:
        model = Quizz
        fields = ()
