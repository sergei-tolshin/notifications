# Generated by Django 3.2 on 2022-06-20 16:24

from django.db import migrations, models
import notices.validators


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='body',
            field=models.TextField(blank=True, help_text='Allowed variables:<br>{{ name }} - user name<br>{{ login }} - user login<br>{{ email }} - user email', validators=[notices.validators.validate_syntax], verbose_name='message body'),
        ),
    ]
