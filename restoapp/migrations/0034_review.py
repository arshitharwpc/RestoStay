# Generated by Django 5.1.5 on 2025-04-01 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restoapp', '0033_rooms'),
    ]

    operations = [
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rev', models.CharField(max_length=255)),
            ],
        ),
    ]
