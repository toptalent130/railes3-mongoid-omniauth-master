# Generated by Django 3.1.7 on 2021-04-10 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0017_auto_20210411_0153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
    ]