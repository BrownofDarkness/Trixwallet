# Generated by Django 4.0 on 2022-12-05 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0003_alter_notification_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notification',
            options={'ordering': ['created_at']},
        ),
    ]