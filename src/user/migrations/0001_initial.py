# Generated by Django 5.1 on 2024-08-23 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pseudo_name', models.CharField(max_length=30)),
                ('pass_word', models.CharField(max_length=12)),
                ('creat_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
