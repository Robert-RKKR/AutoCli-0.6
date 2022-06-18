# Generated by Django 3.2.13 on 2022-06-18 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_alter_devicetypetemplate_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devicetype',
            name='napalm_name',
            field=models.CharField(blank=True, help_text='Napalm name.', max_length=32, null=True, unique=True, verbose_name='Napalm name'),
        ),
        migrations.AlterField(
            model_name='devicetype',
            name='netmiko_name',
            field=models.CharField(blank=True, help_text='Netmiko name.', max_length=32, null=True, unique=True, verbose_name='Netmiko name'),
        ),
    ]
