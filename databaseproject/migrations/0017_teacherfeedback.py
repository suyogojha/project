# Generated by Django 4.0 on 2022-02-16 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databaseproject', '0016_studentpostassignment_alter_postassignments_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='teacherfeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(blank=True, max_length=255, null=True)),
                ('feedback', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]