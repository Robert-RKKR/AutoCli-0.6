# Generated by Django 3.2.13 on 2022-05-15 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='correlated_object',
            field=models.CharField(max_length=64, null=True),
        ),
    ]