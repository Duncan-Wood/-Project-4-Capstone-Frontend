# Generated by Django 4.2 on 2023-04-09 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thrivetracker', '0008_remove_moneytracker_currency_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userstep',
            name='completed',
        ),
    ]