# Generated by Django 4.0.5 on 2022-07-08 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email_token',
        ),
    ]
