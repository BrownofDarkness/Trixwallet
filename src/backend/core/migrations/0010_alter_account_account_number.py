# Generated by Django 4.1.3 on 2022-12-21 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_account_account_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_number',
            field=models.CharField(default='1000001', editable=False, max_length=40, unique=True),
        ),
    ]