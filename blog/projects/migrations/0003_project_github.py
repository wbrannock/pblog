# Generated by Django 2.2.6 on 2019-10-29 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20191023_0149'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='github',
            field=models.CharField(default='www.github.com/wbrannock', max_length=50),
            preserve_default=False,
        ),
    ]