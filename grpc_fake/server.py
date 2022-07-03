import os.path
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from concurrent import futures

import grpc

import messages.movies_pb2_grpc as movies_service
import messages.users_pb2_grpc as users_service
from services.movies import MoviesService
from services.users import UsersService


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    users_service.add_UsersServicer_to_server(UsersService(), server)
    movies_service.add_MoviesServicer_to_server(MoviesService(), server)

    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    print('start')
    serve()
