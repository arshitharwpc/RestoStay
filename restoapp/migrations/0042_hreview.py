# Generated by Django 5.1.5 on 2025-04-02 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restoapp', '0041_pay'),
    ]

    operations = [
        migrations.CreateModel(
            name='hreview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rev', models.CharField(max_length=255)),
            ],
        ),
    ]
