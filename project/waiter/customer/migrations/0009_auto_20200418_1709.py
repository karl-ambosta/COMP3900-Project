# Generated by Django 3.0.3 on 2020-04-18 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_auto_20200417_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlist',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Active'), (2, 'Recieved'), (3, 'Cooking'), (5, 'Completed'), (6, 'Paid')]),
        ),
    ]
