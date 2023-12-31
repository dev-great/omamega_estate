# Generated by Django 3.2 on 2023-11-15 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Listing', '0005_propertylisting_asking_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertylisting',
            name='asking_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True),
        ),
        migrations.AlterField(
            model_name='propertylisting',
            name='rental_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True),
        ),
        migrations.AlterField(
            model_name='propertylisting',
            name='selling_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True),
        ),
    ]
