# Generated by Django 4.0 on 2022-02-15 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('databaseproject', '0012_postassignments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postassignments',
            name='modulecode',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='postassignments',
            name='modulename',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='databaseproject.modulesdetails'),
        ),
    ]
