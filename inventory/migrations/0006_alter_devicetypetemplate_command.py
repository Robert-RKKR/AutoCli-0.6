# Generated by Django 3.2.13 on 2022-05-28 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_auto_20220528_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devicetypetemplate',
            name='command',
            field=models.CharField(help_text='CLI command that will be executed on network device.', max_length=32, verbose_name='CLI command'),
        ),
    ]
