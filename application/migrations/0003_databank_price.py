# Generated by Django 3.0.5 on 2020-04-16 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_remove_databank_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='databank',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Price'),
        ),
    ]
