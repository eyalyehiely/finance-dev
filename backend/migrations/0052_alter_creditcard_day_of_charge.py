# Generated by Django 5.0.4 on 2024-06-18 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0051_alter_creditcard_last_four_digits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcard',
            name='day_of_charge',
            field=models.CharField(choices=[('2', '2'), ('10', '10'), ('15', '15'), ('none', 'none')], max_length=50),
        ),
    ]