# Generated by Django 5.0.4 on 2024-06-14 15:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0049_alter_savings_saving_type'),
        ('users', '0017_remove_customuser_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcard',
            name='family_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='CreditCard', to='users.family'),
        ),
        migrations.AlterField(
            model_name='debts',
            name='family_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='debts', to='users.family'),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='family_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='users.family'),
        ),
        migrations.AlterField(
            model_name='revenues',
            name='family_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='revenue', to='users.family'),
        ),
        migrations.AlterField(
            model_name='savings',
            name='family_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='savings', to='users.family'),
        ),
    ]
