# Generated by Django 5.0.1 on 2024-02-04 04:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problemset', '0003_problem_input_format_problem_memory_limit_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='problem',
            old_name='sameple_intput',
            new_name='sample_intput',
        ),
    ]
