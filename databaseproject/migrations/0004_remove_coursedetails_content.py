# Generated by Django 4.0 on 2022-02-14 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('databaseproject', '0003_coursedetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursedetails',
            name='content',
        ),
    ]