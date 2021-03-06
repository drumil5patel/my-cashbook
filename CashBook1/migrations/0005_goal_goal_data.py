# Generated by Django 3.1.3 on 2022-03-23 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CashBook1', '0004_delete_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('goal_id', models.AutoField(primary_key=True, serialize=False)),
                ('goal_name', models.CharField(max_length=500)),
                ('targeted_amount', models.FloatField()),
                ('create_date', models.DateField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('installment_type', models.IntegerField()),
            ],
            options={
                'db_table': 'Goal',
            },
        ),
        migrations.CreateModel(
            name='Goal_Data',
            fields=[
                ('goal_data_id', models.AutoField(primary_key=True, serialize=False)),
                ('goal_data_date', models.DateField()),
                ('narration', models.CharField(max_length=100)),
                ('cd', models.IntegerField()),
                ('amount', models.FloatField()),
                ('goal_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CashBook1.goal')),
            ],
            options={
                'db_table': 'GoalData',
            },
        ),
    ]
