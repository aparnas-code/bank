# Generated by Django 3.2.19 on 2024-01-12 04:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0003_alter_formdetails_table'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Formdetails',
            new_name='Appformdetails',
        ),
        migrations.AlterModelTable(
            name='appformdetails',
            table='Appformdetails',
        ),
    ]
