# Generated by Django 2.2.6 on 2019-10-05 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrappers', '0006_auto_20191005_2050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='users',
        ),
    ]
