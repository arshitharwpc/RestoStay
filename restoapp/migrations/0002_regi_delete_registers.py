# Generated by Django 4.1.3 on 2025-01-17 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='regi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userfname', models.CharField(max_length=255)),
                ('userlname', models.CharField(max_length=255)),
                ('useremail', models.CharField(max_length=255)),
                ('userphone', models.CharField(max_length=255)),
                ('userpassword', models.CharField(max_length=255)),
                ('hashpass', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='registers',
        ),
    ]
