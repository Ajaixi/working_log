# Generated by Django 2.2.1 on 2020-06-23 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('working_logs', '0010_auto_20200623_0901'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='state',
            field=models.CharField(choices=[('pending', 'pending'), ('reviewed', 'reviewed')], default='pending', max_length=15),
        ),
    ]
