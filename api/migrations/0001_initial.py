# Generated by Django 3.1.4 on 2021-06-08 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('date_start', models.DateField()),
                ('date_end', models.DateField(blank=True, null=True)),
                ('environment', models.CharField(max_length=300)),
                ('activities', models.CharField(max_length=1000)),
                ('magic', models.CharField(max_length=400)),
            ],
        ),
    ]
