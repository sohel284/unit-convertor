# Generated by Django 3.1.1 on 2020-11-24 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unitconverterapp', '0009_auto_20201124_0438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='description',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
