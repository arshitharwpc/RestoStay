# Generated by Django 5.1.5 on 2025-04-01 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restoapp', '0030_lunch'),
    ]

    operations = [
        migrations.CreateModel(
            name='dinner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='media/')),
            ],
        ),
    ]
