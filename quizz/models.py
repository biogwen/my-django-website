from django.db import models

class Email(models.Model):
    email = models.EmailField(verbose_name='your professional email ', max_length=200)

class Quizz(models.Model):
    teamsize = models.IntegerField(verbose_name='Team Size', null=False, max_length=20)
    sprint_time = models.IntegerField(verbose_name='Sprint Time in day', null=False, max_length=20)
    company_size = models.IntegerField(verbose_name='Size of the company', null=False, max_length=20)
    maturity = models.IntegerField(verbose_name='Maturity for 1 (total beginners) to 5 (experts)', null=False, max_length=20)


# Create your models here.
