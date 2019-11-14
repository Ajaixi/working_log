# Generated by Django 2.2.1 on 2019-10-21 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('working_logs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_added',
            field=models.DateTimeField(),
        ),
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_added', models.DateTimeField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='working_logs.Project')),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
        ),
    ]
