# Generated by Django 2.1.2 on 2018-11-11 09:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0005_auto_20181110_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='withhold',
            name='from_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='withhold',
            name='to_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
