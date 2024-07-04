# Generated by Django 4.2.7 on 2024-07-04 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcard',
            name='day_of_charge',
            field=models.CharField(choices=[('2', '2'), ('10', '10'), ('15', '15'), ('אין', 'אין')], max_length=50),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='status',
            field=models.CharField(choices=[('פעיל', 'פעיל'), ('חסום', 'חסום')], max_length=50),
        ),
        migrations.AlterField(
            model_name='debts',
            name='type',
            field=models.CharField(choices=[('משכנתא', 'משכנתא'), ('ממשלתית', 'ממשלתית'), ('הלוואה', 'Loan'), ('עסק', 'עסק'), ('רפואי', 'רפואי'), ('משכון רכב', 'משכון רכב')], max_length=50),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='category',
            field=models.TextField(choices=[('סופר', 'סופר'), ('מסעדה', 'מסעדה'), ('טכנולוגיה', 'טכנולוגיה'), ('הלבשה והנעלה', 'הלבשה והנעלה'), ('דלק', 'דלק'), ('הלוואה', 'הלוואה'), ('חוב', 'חוב'), ('מתנה', 'מתנה')], max_length=50),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='expense_type',
            field=models.CharField(choices=[('הוצאה קבועה', 'הוצאה קבועה'), ('הוצאה משתנה', 'הוצאה משתנה')], max_length=50),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='payment_method',
            field=models.CharField(choices=[('כרטיס אשראי', 'כרטיס אשראי'), ('הוראת קבע', 'הוראת קבע'), ('העברה בנקאית', 'העברה בנקאית'), ('מזומן', 'מזומן'), ('צ׳ק', 'צ׳ק')], max_length=50),
        ),
        migrations.AlterField(
            model_name='revenues',
            name='source',
            field=models.CharField(choices=[('משכורת', 'משכורת'), ('קצבה', 'קצבה'), ('אחר', 'אחר')], max_length=50),
        ),
        migrations.AlterField(
            model_name='savings',
            name='saving_type',
            field=models.CharField(choices=[('בריאות', 'בריאות'), ('עסקים', 'עסקים'), ('רגיל', 'Regular'), ('השכלה', 'השכלה'), ('אחר', 'אחר')], max_length=50),
        ),
    ]
