# Generated by Django 4.0 on 2022-02-14 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databaseproject', '0004_remove_coursedetails_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursedetails',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
