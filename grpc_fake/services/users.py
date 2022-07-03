from messages.users_pb2 import GetUsersResult, User, GetEmailConfirmResult
import messages.users_pb2_grpc as users_service


class UsersService(users_service.UsersServicer):
    def GetUsers(self, request, context):
        return GetUsersResult(
            users=[
                User(id='fd794c08-3d99-4646-9f7a-b4c70e9827ff',
                     name='Nema 1', email='email1@net.net'),
                User(id='fd794c08-3d99-4646-9f7a-b4c70e9827ff',
                     name='Nema 2', email='email2@net.net'),
                User(id='fd794c08-3d99-4646-9f7a-b4c70e9827ff',
                     name='Nema 3', email='email3@net.net'),
                User(id='fd794c08-3d99-4646-9f7a-b4c70e9827ff',
                     name='Nema 4', email='email4@net.net'),
                User(id='fd794c08-3d99-4646-9f7a-b4c70e9827ff',
                     name='Nema 5', email='email5@net.net'),
                User(id='fd794c08-3d99-4646-9f7a-b4c70e9827ff',
                     name='Nema 6', email='email6@net.net'),
                User(id='fd794c08-3d99-4646-9f7a-b4c70e9827ff',
                     name='Nema 7', email='email7@net.net'),
                User(id='fd794c08-3d99-4646-9f7a-b4c70e9827ff',
                     name='Nema 8', email='email8@net.net'),
                User(id='fd794c08-3d99-4646-9f7a-b4c70e9827ff',
                     name='Nema 9', email='email9@net.net'),
                User(id='fd794c08-3d99-4646-9f7a-b4c70e9827ff',
                     name='Nema 0', email='email0@net.net')
            ]
        )

    def GetEmailConfirm(self, request, context):
        if request.id:
            """
            Поиск пользователя и формирование которкой ссылки происходит
            в сервисе авторизации.
            Ссылка формируется и сохраняется в базу, затем при помощи
            библиотеки hashids формируется короткая ссылка
            """
            return GetEmailConfirmResult(
                name='Gadya Hrenova',
                email='user@fake.ru',
                link='https://example.com//b8NwYzA'
            )
