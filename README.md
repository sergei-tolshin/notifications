
# Сервис для отправки уведомлений
Сервис уведомлений пользователей о различного рода событиях,
будь то недосмотренные фильмы, выход новой серии сериала, пятничная подборка топ-10 за неделю
или чек об оплате подписки.

### Технологии
* #### Фреймворки
    * Django
    * FastAPI
    * Celery
* #### Движок шаблонов
    * Jinja2
* #### Базы данных
    * PostgreSQL
* #### Брокер сообщений
    * RabbitMQ
* #### Прокси сервер
    * Nginx
* #### Обмен данными между сервисами
    * REST API
    * gRPC

### Компоненты системы нотификации
#### Админ-панель
Админ-панель построена на безе Django.

Она помогает администраторам и менеджерам онлайн кинотеатра производить некоторые настройки системы уведомлений.

Администраторы имеют возможность подключать сервисы, генерирующие события, а так же настраивать возможные каналы отправки уведомлений на основе события.

У менеджеров есть возможность создавать рассылки предложений и новостей для пользователей, с возможностью установки даты и времени начала рассылки.
Кроме того менеджеры могут создавать и редактировать шаблоны уведомлений с использованием подстановочных переменных, например:
* {{ name }} - имя пользователя
* {{ email }} - адрес почты
* {{ link }} - ссылка

#### API для приёма событий по созданию уведомлений
Для создания API была использована связка FastAPI и Celery.
API принимает события от других микросервисов системы кинотеатра и помещает информацию о событии в брокер сообщений RabbitMQ для дальнейшей отправки уведомления пользователю.

В API предусмотрена два эндпоинта:
* **[POST]** `/api/v1/notices/send` - прием события для помещения в очередь  
    Принимает на вход:
    ```
    {
      "app": "auth",
      "event": "registration",
      "notice_method": [
        "email"
      ],
      "payload": {
        "user_id": "fd794c08-3d99-4646-9f7a-b4c70e9827ff"
      }
    }
    ```
    и возвращает id задачи на отправку уведомления `{'notice_id': <id>}`

* **[GET]** `/api/v1/notices/{notice_id}` - получить статус уведомления и результат, если возвращается  
    Принимает `notice_id` и в ответ отдает:
    ```
    {
        'notice_id': <id>,
        'notice_status': <status>,
        'notice_result': <result>
    }
    ```

Благодаря встроенным возможностям FastAPI, будет автоматически создана документация по api. 
После запуска приложения посмотреть все доступные эндпоинты и протестировать его работу можно прямо в браузере. 
Для этого откройте страницу http://0.0.0.0/api/openapi

#### Scheduler - генератор автоматических событий
Шедулер реализован на Django и Celery.

Он мониторит БД, достает задания уведомлений, которые нужно отправить и помещает их в очередь сообщений.

В админ-панели существует функционал для создания переодических задач шедулера, где можно настроить период или точную дату и время выполнения задачи на отправку уведомлений.

Так же при создании задачи есть возможность указать данные для задачи, например группу пользователей, которым необходимо отсылать уведомление.

#### Worker - процесс, который отправляет уведомление
Воркер так же как и шедулер подключен к Django и использует Celery.

Воркер получает задачи уведомлений из очереди сообщений RabbitMQ.
На основе полученной задачи, он получает нужный шаблон уведомления.
На основе дополнительных данных задачи, воркер может запрашивать необходимую информацию из других сервисов по gRPC, таких как Auth (система авторизации), Movies (каталог фильмов), UGC (система пользовательского контента).
После получения всех неоходимых данных, воркер рендерит шаблоны с помощью модуля Jinja2 и отправляет уведомление через нужный канал связи (E-mail, SMS, Websocket)

---

### Вспомогательный модуль gRPC сервер (grpc_fake)
Этот модуль не является компонентом системы нотификации, 
он просто эмитирует отдачу данных, запрошенных системой нотификации из других сервисов.

На данный момент в нем релизована отдача информации о пользователях и фильмах.

Поместив необходимые файлы в соответствующие сервисы (Auth и Movies) и 
доработав в файлах `notifications/grpc_fake/services/users.py` и `notifications/grpc_fake/services/movies.py` полчение необходимых данных для отдачи, можно поднять gRPC сервер на каждом сервисе.

---

### Запуск приложения
Для запуска приложения выполните:

1. склонируйте или скопируйте в репозиторий
```bash
$ git clone 'путь до репозитория'
```
2. Создайте .env файл и заполните его аналогично .env.example.
3. Запустите сборку
```
docker-compose up -d --build
```
Докер соберет необходимые образы и запустит контейнеры.

После запуска будут доступны:
* Админ-панель: http://127.0.0.1:58000/admin/
* Swagger API: http://127.0.0.1/api/openapi/
* RabbitMQ Management: http://127.0.0.1:15672/
* Панель мониторинга Flower: http://127.0.0.1:5556/