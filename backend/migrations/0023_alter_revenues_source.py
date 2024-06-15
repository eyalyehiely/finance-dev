# Generated by Django 5.0.4 on 2024-06-04 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0022_delete_business'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revenues',
            name='source',
            field=models.CharField(choices=[('salary', 'משכורת'), ('allowance', 'קצבה'), ('other', 'אחר')], max_length=50),
        ),
    ]
