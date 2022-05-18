# Generated by Django 3.2.13 on 2022-05-15 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('application', models.CharField(max_length=64)),
                ('severity', models.IntegerField(choices=[(1, 'CRITICAL'), (2, 'ERROR'), (3, 'WARNING'), (4, 'INFO'), (5, 'DEBUG')])),
                ('message', models.CharField(max_length=1024)),
                ('correlated_object', models.CharField(max_length=64)),
                ('task_id', models.CharField(max_length=64, null=True)),
                ('user_message', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Log',
                'verbose_name_plural': 'Logs',
                'permissions': [],
                'default_permissions': ['read_only', 'read_write'],
            },
        ),
        migrations.CreateModel(
            name='LogDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('value', models.CharField(max_length=128)),
                ('log', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logger.log')),
            ],
            options={
                'verbose_name': 'Log detail',
                'verbose_name_plural': 'Logs details',
                'permissions': [],
                'default_permissions': ['read_only', 'read_write'],
            },
        ),
    ]