# Generated by Django 3.2.19 on 2024-01-12 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0005_auto_20240112_1014'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=200)),
            ],
        ),
    ]
