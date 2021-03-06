# Generated by Django 3.1.3 on 2022-03-23 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CashBook1', '0008_goal_cur'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='achieved_amount',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='goal',
            name='remaining_amount',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
