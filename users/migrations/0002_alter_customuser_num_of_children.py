# Generated by Django 5.0.4 on 2024-06-28 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='num_of_children',
            field=models.IntegerField(default=0),
        ),
    ]
