# Generated by Django 2.2.6 on 2019-10-29 01:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_github'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='image',
        ),
    ]
