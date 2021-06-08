from rest_framework import serializers

from .models import Cv

class CvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cv
        fields= ('position', 'company', 'date_start', 'date_end', 'environment', 'activities', 'magic')


