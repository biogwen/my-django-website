from django.db import models

class Email(models.Model):
    email = models.EmailField(verbose_name='your professional email ', max_length=200)

class Quizz(models.Model):
    teamsize = models.IntegerField(verbose_name='Team Size', null=True)
    sprint_time = models.IntegerField(verbose_name='Sprint duration in days', null=True)
    company_size = models.IntegerField(verbose_name='Company size', null=True)
    maturity = models.IntegerField(verbose_name='Agile maturity from 1 (total beginners) to 5 (experts)', null=True)



# Create your models here.
