# Generated by Django 3.2 on 2022-07-02 06:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('django_celery_beat', '0016_alter_crontabschedule_timezone'),
        ('notices', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('subject', models.CharField(max_length=100, verbose_name='subject')),
                ('clocked_time', models.DateTimeField(default=django.utils.timezone.now, help_text='run the newsletter at the set time', verbose_name='clock time')),
                ('recipients', models.JSONField(help_text="Example of a recipient filter:<br>{<br>   'emails': ['user1@fake.ru', ..., 'userN@fake.ru'],<br>   'groups': ['paid subscription'],<br>   'age': ['gte=18', 'lt=35'],<br>   'cities': ['Moscow', 'Ekaterinburg']<br>}", verbose_name='recipients')),
                ('enabled', models.BooleanField(default=True, verbose_name='enabled')),
                ('task', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='django_celery_beat.periodictask')),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='newsletters', to='notices.template', verbose_name='template')),
            ],
            options={
                'verbose_name': 'newsletter',
                'verbose_name_plural': 'newsletters',
                'db_table': 'notice"."newsletter',
            },
        ),
    ]
