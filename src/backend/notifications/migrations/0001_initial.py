# Generated by Django 4.1.3 on 2022-11-29 14:39

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
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=800)),
                ('type', models.CharField(choices=[('NORMAL', 'NORMAL'), ('TRANSFER', 'TRANSFER'), ('TRANSFER_SUCCESSFULL', 'TRANSFER_SUCCESSFULL'), ('TRANSFER_REJECTED', 'TRANSFER_REJECTED'), ('WITHDRAW', 'WITHDRAW'), ('WITHDRAW_REJECTED', 'WITHDRAW_REJECTED'), ('WITHDRAW_CANCEL', 'WITHDRAW_CANCEL'), ('WITHDRAW_SUCCESSFULL', 'WITHDRAW_SUCCESSFULL'), ('WITHDRAW_CANCEL', 'WITHDRAW_CANCEL'), ('ACCOUNT_EMPTY', 'ACCOUNT_EMPTY'), ('ALERT', 'ALERT')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]