# Generated by Django 2.2.1 on 2020-06-08 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('working_logs', '0008_auto_20191120_1936'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thumb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_url', models.FileField(blank=True, null=True, upload_to='thumbs/')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='working_logs.Project')),
            ],
            options={
                'verbose_name_plural': 'Thumbs',
            },
        ),
    ]
