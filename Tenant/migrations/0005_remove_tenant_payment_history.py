# Generated by Django 3.2 on 2023-12-10 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tenant', '0004_auto_20231210_2235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tenant',
            name='payment_history',
        ),
    ]
