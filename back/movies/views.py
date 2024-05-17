from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import MovieListSerializer, MovieSerializer
from .models import Movie

from rest_framework.views import APIView
from rest_framework import status
from .utils import fetch_and_save_movies

# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializers = MovieListSerializer(movies, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie_detail(request, movie_pk):
    if request.method == 'GET':
        movie = Movie.objects.get(pk=movie_pk)
        serializers = MovieListSerializer(movie)
        return Response(serializers.data)
    


class FetchMoviesAPIView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            fetch_and_save_movies()
            return Response({'status': 'success'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
