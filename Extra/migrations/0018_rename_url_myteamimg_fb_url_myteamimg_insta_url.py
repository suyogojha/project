# Generated by Django 4.0 on 2022-02-06 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Extra', '0017_myteamimg_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myteamimg',
            old_name='url',
            new_name='fb_url',
        ),
        migrations.AddField(
            model_name='myteamimg',
            name='insta_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
