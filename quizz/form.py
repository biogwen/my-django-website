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


class Quizagile(forms.ModelForm):
    class Meta:
        model = Quizz
        fields = ('__all__')

    def clean_maturity(self):
        maturity = self.cleaned_data['maturity']

        if maturity < 1:
            raise ValidationError("You can't be so bad")

        elif maturity > 5:
            raise ValidationError("Are you sure you are more than an expert?")

        return maturity

    def clean_company_size(self):
        company = self.cleaned_data['company_size']
        team = self.cleaned_data['teamsize']

        if company < team:
            raise ValidationError("Your team is bigger than your company. Please take into account everyone!")

        return company
