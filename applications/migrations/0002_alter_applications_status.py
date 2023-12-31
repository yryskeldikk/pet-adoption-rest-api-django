# Generated by Django 4.2.7 on 2023-11-13 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('denied', 'Denied'), ('withdrawn', 'Withdrawn')], default='pending', max_length=50),
        ),
    ]
