# Generated by Django 4.1.4 on 2023-02-27 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_doctor_profilepic_alter_patient_profilepic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='Firstname',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='Lastname',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='Firstname',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='Lastname',
        ),
    ]
