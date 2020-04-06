# Generated by Django 3.0.4 on 2020-04-04 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profile_id',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
