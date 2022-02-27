# Generated by Django 4.0 on 2022-01-20 12:40

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_myportfilio_new_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myportfilio',
            name='new_slug',
        ),
        migrations.AddField(
            model_name='myblog',
            name='new_slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='title', unique=True),
        ),
    ]