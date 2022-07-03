import messages.movies_pb2_grpc as movies_service
from messages.movies_pb2 import Genre, GetMoviesResult, Movie, Person


class MoviesService(movies_service.MoviesServicer):
    def GetMovies(self, request, context):
        for movie in request.movies:
            movie = Movie(
                id=movie.id,
                title='Titanik',
                description='Караблик утанул(',
                rating='9.5',
                genres=[Genre(name='drama'), Genre(name='camedy')],
                persons=[
                    Person(full_name='actor 1', role='actor'),
                    Person(full_name='actor 2', role='director')
                ]
            )
            yield GetMoviesResult(movies=movie)
