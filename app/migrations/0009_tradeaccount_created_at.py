# Generated by Django 3.1.7 on 2021-04-11 08:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_usertradeaccount'),
    ]

    operations = [
        migrations.AddField(
            model_name='tradeaccount',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
