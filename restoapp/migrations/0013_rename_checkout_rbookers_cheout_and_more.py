# Generated by Django 4.1.3 on 2025-03-06 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restoapp', '0012_rename_checkin_rbookers_chein'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rbookers',
            old_name='checkout',
            new_name='cheout',
        ),
        migrations.RenameField(
            model_name='rbookers',
            old_name='specialreq',
            new_name='req',
        ),
    ]
