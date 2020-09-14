# Generated by Django 3.1 on 2020-09-14 18:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0011_checkout_purchase_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='purchase_date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
