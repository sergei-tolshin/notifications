# Generated by Django 3.2 on 2022-06-18 12:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('method', models.CharField(choices=[('email', 'E-mail'), ('sms', 'SMS'), ('telegram', 'Telegram'), ('websocket', 'Websocket')], default='email', max_length=20, verbose_name='delivery method')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='name')),
                ('body', models.TextField(blank=True, verbose_name='message body')),
            ],
            options={
                'verbose_name': 'template',
                'verbose_name_plural': 'templates',
                'db_table': 'notice"."template',
            },
        ),
    ]
