# Generated by Django 5.1 on 2024-08-26 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='birth_date',
        ),
    ]
