# Generated by Django 2.2.4 on 2020-07-27 06:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0129_tribessubscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='hackathonevent',
            name='border_color',
            field=models.CharField(blank=True, help_text='hexcode for the border, default to none', max_length=255, null=True),
        ),
    ]
