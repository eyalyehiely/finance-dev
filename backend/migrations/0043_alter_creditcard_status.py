# Generated by Django 5.0.4 on 2024-06-10 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0042_alter_creditcard_credit_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcard',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Blocked', 'Blocked')], max_length=50),
        ),
    ]
