from core.utils.translation import gettext_lazy as _
from fastapi import APIRouter, Depends, HTTPException, Request, status
# from models.favorites import Favorite
from services.notices import NoticesService, get_notices_service
from celery.result import AsyncResult
router = APIRouter()


# @router.get('/favorites/',
#             summary='Список избранных фильмов',
#             description='Просмотр списка избранных фильмов',
#             status_code=status.HTTP_200_OK)
# async def list_favorites(
#     request: Request,
#     service: NoticesService = Depends(get_notices_service)
# ):
#     fields = {
#         '_id': False,
#         'movie_id': True
#     }
#     favorites = await service.list({'user_id': request.user.identity}, fields)
#     return [_['movie_id'] for _ in favorites]

@router.get('/tasks/{task_id}')
async def get_status(
    task_id,
    service: NoticesService = Depends(get_notices_service)
):
    task_result = AsyncResult(task_id, app=service.producer)
    result = {
        'task_id': task_id,
        'task_status': task_result.status,
        'task_result': task_result.result
    }
    return result


@router.post('/',
             summary='Тестовое уведомление',
             description='Отправить тестовое уведомление',
             status_code=status.HTTP_201_CREATED)
async def send_test(
    name: str,
    request: Request,
    service: NoticesService = Depends(get_notices_service)
):
    task = await service.send_notice(name)
    return {'task_id': task.id}
