# Generated by Django 3.1 on 2020-09-17 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0016_remove_checkout_program'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='total_cost',
        ),
        migrations.AddField(
            model_name='checkoutlineitem',
            name='program_cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AddField(
            model_name='checkoutlineitem',
            name='total_cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]
