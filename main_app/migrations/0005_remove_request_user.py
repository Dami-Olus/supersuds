# Generated by Django 4.2.4 on 2023-10-04 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_request_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='user',
        ),
    ]