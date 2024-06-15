# Generated by Django 5.0.4 on 2024-06-06 08:08

from django.db import migrations, models
import datetime

class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0023_alter_revenues_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='debts',
            name='starting_date',
             field=models.DateField(default=datetime.date(2013, 1, 1)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loans',
            name='starting_date',
             field=models.DateField(default=datetime.date(2013, 1, 1)),
            preserve_default=False,
        ),
    ]
