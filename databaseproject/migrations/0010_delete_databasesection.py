# Generated by Django 4.0 on 2022-02-15 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('databaseproject', '0009_rename_section_databasesection_modulecode_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='databasesection',
        ),
    ]