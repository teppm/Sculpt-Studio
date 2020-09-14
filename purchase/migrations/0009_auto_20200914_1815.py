# Generated by Django 3.1 on 2020-09-14 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0004_auto_20200821_1504'),
        ('purchase', '0008_auto_20200913_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='program',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='programs.programs'),
        ),
    ]
