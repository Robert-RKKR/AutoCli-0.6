# Generated by Django 3.2.13 on 2022-05-26 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20220526_1304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devicetypetemplate',
            name='device_type',
        ),
        migrations.AddField(
            model_name='devicetype',
            name='device_type_templates',
            field=models.ManyToManyField(blank=True, help_text='All devices type templates.', to='inventory.DeviceTypeTemplate', verbose_name='Device type template/s'),
        ),
    ]
