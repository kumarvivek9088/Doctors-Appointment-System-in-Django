# Generated by Django 4.1.4 on 2023-03-01 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='public',
            field=models.BooleanField(default=False),
        ),
    ]