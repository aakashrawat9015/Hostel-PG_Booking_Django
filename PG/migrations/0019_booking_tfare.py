# Generated by Django 4.1.5 on 2023-02-20 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PG', '0018_booking_a_date_booking_month'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='tfare',
            field=models.IntegerField(default=0),
        ),
    ]