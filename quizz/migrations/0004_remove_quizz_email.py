# Generated by Django 3.1.4 on 2021-06-28 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizz', '0003_auto_20210628_0836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizz',
            name='email',
        ),
    ]
