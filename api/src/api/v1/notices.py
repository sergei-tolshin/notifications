from celery.result import AsyncResult
from fastapi import APIRouter, Depends, status
from models.event import Event
from services.notices import NoticesService, get_notices_service

router = APIRouter()


@router.get('/{notice_id}',
            summary='Статус отправки уведомления',
            description='Получить статус отправки уведомления',
            )
async def get_status(
    notice_id,
    service: NoticesService = Depends(get_notices_service)
):
    notice_result = AsyncResult(notice_id, app=service.producer)
    result = {
        'notice_id': notice_id,
        'notice_status': notice_result.status,
        'notice_result': notice_result.result
    }
    return result


@router.post('/send',
             summary='Создание уведомления',
             description='Создать уведомление по принятому событию',
             status_code=status.HTTP_201_CREATED)
async def send_test(
    event: Event,
    service: NoticesService = Depends(get_notices_service)
):
    notice = await service.send_notice(event)
    return {'notice_id': notice.id}
