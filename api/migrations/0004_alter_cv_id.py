# Generated by Django 4.0 on 2021-12-07 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210614_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
