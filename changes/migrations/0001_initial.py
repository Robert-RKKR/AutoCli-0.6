# Generated by Django 3.2.13 on 2022-06-23 21:36

import autocli.basemodel.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Change',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Model create date.', verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Model last update date.', verbose_name='Updated')),
                ('deleted', models.BooleanField(default=False)),
                ('root', models.BooleanField(default=False, help_text='Model with root option cannot be deleted.', verbose_name='Root')),
                ('active', models.BooleanField(default=True, help_text='Status of Model object.', verbose_name='Active')),
                ('name', models.CharField(error_messages={'blank': 'Name field is mandatory.', 'invalid': 'Enter the correct name value. It must contain 3 to 32 digits, letters or special characters -, _ or spaces.', 'null': 'Name field is mandatory.', 'unique': 'Object with this name already exists.'}, help_text='Model name.', max_length=32, unique=True, validators=[autocli.basemodel.validators.NameValueValidator()], verbose_name='Name')),
                ('description', models.CharField(default='Model description.', error_messages={'invalid': 'Enter the correct description value. It must contain 8 to 256 digits, letters and special characters -, _, . or spaces.'}, help_text='Model description.', max_length=256, validators=[autocli.basemodel.validators.DescriptionValueValidator()], verbose_name='Description')),
                ('model_name', models.CharField(help_text='CLI command name.', max_length=64, verbose_name='Command name')),
                ('object_name', models.CharField(help_text='CLI command name.', max_length=64, verbose_name='Command name')),
                ('before', models.JSONField(help_text='CLI command name.', max_length=64, verbose_name='Command name')),
                ('after', models.JSONField(blank=True, help_text='CLI command raw data output.', null=True, verbose_name='Command raw data')),
                ('administrator', models.ForeignKey(help_text='Administrator responsible for change.', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Administrator')),
            ],
            options={
                'verbose_name': 'Change',
                'verbose_name_plural': 'Changes',
            },
        ),
    ]
