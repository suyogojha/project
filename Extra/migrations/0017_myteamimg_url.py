# Generated by Django 4.0 on 2022-02-06 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Extra', '0016_myteamimg_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='myteamimg',
            name='url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]