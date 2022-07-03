# API системы нотификации
Ендпоинты:
 - [POST] /api/v1/notices/send - Создание уведомления
 - [GET] /api/v1/notices/{notice_id} - Статус отправки уведомления

Принимает на вход запрос вида:
```
    {
      "app": "auth",
      "event": "registration",
      "notice_method": [
        "email"
      ],
      "payload": {
        "user_id": "fd794c08-3d99-4646-9f7a-b4c70e9827ff",
        "email": "user@fake.ru"
      }
    }
```