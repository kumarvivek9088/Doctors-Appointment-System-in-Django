# Generated by Django 4.1.4 on 2023-04-29 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_alter_appointment_starttime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='starttime',
            field=models.DateTimeField(null=True),
        ),
    ]