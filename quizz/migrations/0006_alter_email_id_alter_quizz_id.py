# Generated by Django 4.0 on 2021-12-07 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizz', '0005_auto_20210705_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='quizz',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
