# Generated by Django 3.2 on 2023-12-16 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authorization', '0007_alter_customuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]
