# Generated by Django 3.0.5 on 2020-04-23 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0008_auto_20200423_0557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='databank',
            name='contact',
            field=models.IntegerField(null=True, verbose_name='Phone Number (Your phone number will show up on your Ad.)'),
        ),
    ]
