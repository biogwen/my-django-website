from django.db import models

class Email(models.Model):
    email = models.EmailField(max_length=200)

class Quizz(models.Model):
    teamsize = models.IntegerField(null=False)
    sprint_time = models.IntegerField(null=False)
    company_size = models.IntegerField(null=False)
    maturity = models.IntegerField(null=False)


# Create your models here.
