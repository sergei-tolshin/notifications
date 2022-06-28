import time

from celery import shared_task


# Задача отправки уведомления для подтверждения электронной почты
# @shared_task(bind=True, name='confirm_email', default_retry_delay=60 * 5, max_retries=5)
# def confirm_email(self, user_id):
#     # self.request.task_name = 'confirm_email'
#     try:
#         print("doing stuff here...")
#     except SomeNetworkException as error:
#         print("maybe do some clenup here....")
#         self.retry(error)

@shared_task(bind=True, name='tasks.test', default_retry_delay=60 * 5, max_retries=5)
def test(self, name):
    print(f"doing stuff here... {name}")


# Задача Отправка письма о лайке комментария клиента (единичное, можно отложить)
# Задача Еженедельная рассылка перед выходными (переодическое)
# Задача Ручная рассылка от менеджера (единичное, мгновенное)
# Задача Вышла новая серия сериала, который смотрит пользователь (единичное, мгновенное)

# Уведомления:
#  - Подтверждение электронной почты (персональное, единичное, мгновенное) [канал: email]
#  - Подтверждение телефона (персональное, единичное, мгновенное) [канал: sms]
#  - Статус платежа подписки, чек об оплате (персональное, единичное, мгновенное) [канал: email, websocket]

#  - Уведомления о новых фильмах и сериалах (групповове, единичное, мгновенное) [канал: email, websocket]
#  - Уведомления о ТОП-10 фильмов недели (групповове, периодическое по расписанию) [канал: email, websocket]
#  - Уведомления о новых лайках рецензии пользователя (персональное, единичное, отложенное) [канал: email, websocket]

#  - Рекламные уведоления созданные менеджерами (групповове, единичное, мгновенное) (канал: email, websocket]