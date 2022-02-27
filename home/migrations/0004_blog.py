# Generated by Django 4.0 on 2022-01-02 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_contactus_message_contactus_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('content', models.CharField(blank=True, max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]