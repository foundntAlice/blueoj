# Generated by Django 5.0.1 on 2024-02-04 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problemset', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='public_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='time_limit',
            field=models.IntegerField(null=True),
        ),
    ]