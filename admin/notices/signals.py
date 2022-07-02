import json

from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from django_celery_beat.models import ClockedSchedule, PeriodicTask

from .models import Newsletter


@receiver(pre_save, sender=Newsletter)
def create_periodic_task(sender, instance, **kwargs):
    if instance.task is None:
        clocked_time = ClockedSchedule.objects.create(
            clocked_time=instance.clocked_time)
        instance.task = PeriodicTask.objects.create(
            name=instance.title,
            task='promo.newsletter',
            clocked=clocked_time,
            one_off=True,
            kwargs=json.dumps({
                'template_id': str(instance.template.id),
                'subject': instance.subject,
                'recipients': instance.recipients
            }, ensure_ascii=False,),
            start_time=timezone.now()
        )
    else:
        instance.task.clocked.clocked_time = instance.clocked_time
        instance.task.enabled = instance.enabled is True
        instance.task.kwargs = json.dumps({
            'template_id': str(instance.template.id),
            'subject': instance.subject,
            'recipients': instance.recipients
        }, ensure_ascii=False,)
        instance.task.clocked.save()
        instance.task.save()
