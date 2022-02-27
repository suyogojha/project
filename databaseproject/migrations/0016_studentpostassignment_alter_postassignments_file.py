# Generated by Django 4.0 on 2022-02-15 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databaseproject', '0015_alter_postassignments_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='studentpostassignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentname', models.CharField(blank=True, max_length=255, null=True)),
                ('modulename', models.CharField(blank=True, max_length=255, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='upload/Assignmentque')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='postassignments',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='upload/Assignmentque'),
        ),
    ]