# Generated by Django 5.0.4 on 2024-06-06 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0027_remove_loans_num_of_months_loans_finish_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='debts',
            name='debt_type',
            field=models.CharField(choices=[('mortgage', 'משכנתא'), ('goverment', 'ממשלתית'), ('loan', 'הלוואה'), ('business', 'עסק'), ('medical', 'רפואי'), ('car', 'משכון רכב')], default='default', max_length=50),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Loans',
        ),
    ]
