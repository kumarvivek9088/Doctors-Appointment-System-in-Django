# Generated by Django 4.1.4 on 2023-04-29 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_remove_appointment_starttime_appointment_dt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='dt',
            field=models.DateField(auto_now_add=True),
        ),
    ]
