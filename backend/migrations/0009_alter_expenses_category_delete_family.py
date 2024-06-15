# Generated by Django 5.0.4 on 2024-04-30 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_debts_alter_business_debt_alter_family_debt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='category',
            field=models.TextField(choices=[('supermarket', 'סופר'), ('restaurant', 'מסעדה'), ('tech', 'טכנולוגיה'), ('dress and shoes', 'הלבשה והנעלה'), ('fuel', 'דלק'), ('loan', 'הלוואה'), ('debt', 'חוב'), ('gift', 'מתנה')], max_length=50),
        ),
        migrations.DeleteModel(
            name='Family',
        ),
    ]
