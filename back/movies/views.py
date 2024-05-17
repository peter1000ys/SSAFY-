from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import MovieListSerializer, MovieSerializer
from .models import Movie

from rest_framework.views import APIView
from rest_framework import status
from .utils import fetch_and_save_movies, fetch_and_save_genres

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
    
# TMDB에서 장르 가져오기 위한 view함수
class FetchGenresAPIView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            fetch_and_save_genres()
            return Response({'status': 'success'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
# TMDB에서 영화 정보 가져오기 위한 view 함수
class FetchMoviesAPIView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            fetch_and_save_movies()
            return Response({'status': 'success'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
