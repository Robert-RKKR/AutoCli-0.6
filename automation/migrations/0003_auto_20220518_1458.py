# Generated by Django 3.2.13 on 2022-05-18 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0002_auto_20220518_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='deviceupdate',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='policyrunner',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='policytask',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]