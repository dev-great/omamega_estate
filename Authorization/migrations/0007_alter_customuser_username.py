# Generated by Django 3.2 on 2023-12-10 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authorization', '0006_alter_customuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(blank=True, default=True, max_length=30, null=True),
        ),
    ]
