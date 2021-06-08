from django.db import models

class Cv(models.Model):
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    date_start = models.DateField(null=False, blank=False)
    date_end = models.DateField(null=True, blank=True)
    environment = models.CharField(max_length=300)
    activities = models.CharField(max_length=1000)
    magic = models.CharField(max_length=400)


    def __str__(self):
        return self.position
# Create your models here.
