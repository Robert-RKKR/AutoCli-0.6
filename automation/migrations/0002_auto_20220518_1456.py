# Generated by Django 3.2.13 on 2022-05-18 14:56

import autocli.basemodel.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_celery_beat', '0015_edit_solarschedule_events_choices'),
        ('inventory', '0003_auto_20220518_1450'),
        ('automation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Model create date.', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Model last update date.', verbose_name='Updated')),
                ('deleted', models.BooleanField(default=False)),
                ('root', models.BooleanField(default=False, help_text='Model with root option cannot be deleted.', verbose_name='Root')),
                ('active', models.BooleanField(default=True, help_text='Status of Model object.', verbose_name='Active')),
                ('name', models.CharField(error_messages={'blank': 'Name field is mandatory.', 'invalid': 'Enter the correct name value. It must contain 3 to 32 digits, letters or special characters -, _ or spaces.', 'null': 'Name field is mandatory.', 'unique': 'Object with this name already exists.'}, help_text='Model name.', max_length=32, unique=True, validators=[autocli.basemodel.validators.NameValueValidator()], verbose_name='Name')),
                ('description', models.CharField(default='Model description.', error_messages={'invalid': 'Enter the correct description value. It must contain 8 to 256 digits, letters and special characters -, _, . or spaces.'}, help_text='Model description.', max_length=256, validators=[autocli.basemodel.validators.DescriptionValueValidator()], verbose_name='Description')),
                ('devices', models.ManyToManyField(blank=True, help_text='Xxx.', to='inventory.Device', verbose_name='Corelated device/s')),
                ('folders', models.ManyToManyField(blank=True, help_text='Xxx.', to='inventory.Folder', verbose_name='Corelated folder/s')),
                ('scheduler', models.ForeignKey(blank=True, help_text='Task scheduler.', null=True, on_delete=django.db.models.deletion.CASCADE, to='django_celery_beat.intervalschedule', verbose_name='Scheduler')),
            ],
            options={
                'verbose_name': 'Policy',
                'verbose_name_plural': 'Polices',
            },
        ),
        migrations.CreateModel(
            name='PolicyTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Model create date.', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Model last update date.', verbose_name='Updated')),
                ('result_status', models.BooleanField(default=False, help_text='A positive result means that the commands output match TextFSM and Regex expression.', verbose_name='Result status')),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
            },
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Model create date.', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Model last update date.', verbose_name='Updated')),
                ('deleted', models.BooleanField(default=False)),
                ('root', models.BooleanField(default=False, help_text='Model with root option cannot be deleted.', verbose_name='Root')),
                ('active', models.BooleanField(default=True, help_text='Status of Model object.', verbose_name='Active')),
                ('name', models.CharField(error_messages={'blank': 'Name field is mandatory.', 'invalid': 'Enter the correct name value. It must contain 3 to 32 digits, letters or special characters -, _ or spaces.', 'null': 'Name field is mandatory.', 'unique': 'Object with this name already exists.'}, help_text='Model name.', max_length=32, unique=True, validators=[autocli.basemodel.validators.NameValueValidator()], verbose_name='Name')),
                ('description', models.CharField(default='Model description.', error_messages={'invalid': 'Enter the correct description value. It must contain 8 to 256 digits, letters and special characters -, _, . or spaces.'}, help_text='Model description.', max_length=256, validators=[autocli.basemodel.validators.DescriptionValueValidator()], verbose_name='Description')),
                ('template', models.TextField(help_text='CLI command/s template.', verbose_name='CLI template')),
                ('sfm_expression', models.TextField(help_text='SFM expression used to check if CLI command/s output is correct.', verbose_name='SFM expression')),
                ('regex_expression', models.TextField(help_text='Regex expression used to check if CLI command/s output is correct.', verbose_name='Regex expression')),
            ],
            options={
                'verbose_name': 'Template',
                'verbose_name_plural': 'Templates',
            },
        ),
        migrations.CreateModel(
            name='PolicyRunner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Model create date.', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Model last update date.', verbose_name='Updated')),
                ('status', models.IntegerField(choices=[(0, 'Initiation'), (1, 'Collecting data'), (2, 'Saved data')], default=0, help_text='Policy manager status.', verbose_name='Update status')),
                ('result_status', models.BooleanField(default=False, help_text='A positive result means that all of the commands output match TextFSM and Regex expression.', verbose_name='Result status')),
                ('policy', models.ForeignKey(help_text='Xxx.', on_delete=django.db.models.deletion.CASCADE, to='automation.policy', verbose_name='Xxx')),
            ],
            options={
                'verbose_name': 'Policy manager',
                'verbose_name_plural': 'Policy managers',
            },
        ),
        migrations.AddField(
            model_name='policy',
            name='templates',
            field=models.ManyToManyField(blank=True, help_text='Xxx.', to='automation.Template', verbose_name='Corelated template/s'),
        ),
    ]