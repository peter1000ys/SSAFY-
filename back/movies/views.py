from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import MovieListSerializer, MovieSerializer, GenreListSerializer
from .models import Movie,Genre
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.views import APIView
from rest_framework import status
from .utils import fetch_and_save_movies, fetch_and_save_genres

# Create your views here.
@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie.objects.order_by('-popularity')[:30])
        serializers = MovieListSerializer(movies, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def movie_detail(request, movie_pk):
    if request.method == 'GET':
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

@api_view(['GET'])
def genre_list(request):
    if request.method == 'GET':
        genres = get_list_or_404(Genre)
        serializers = GenreListSerializer(genres, many=True)
        return Response(serializers.data)

@api_view(['GET'])
def filter_genre(request, genre_pk):
    if request.method == 'GET':
        movies = get_list_or_404(Movie.objects.order_by('-popularity'), genres = genre_pk)
        serializers = MovieListSerializer(movies, many=True)
        return Response(serializers.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movie_likes(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    user = request.user
    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
        like = False
    else:
        movie.like_users.add(user)
        like = True
    like_status = {
        'liked': like,
        'count': movie.like_users.count(),
    }
    return JsonResponse(like_status)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movie_hates(request, movie_id, user_pk):
    movie = get_object_or_404(Movie, pk=movie_id)
    user = request.user
    if movie.hate_users.filter(pk=user.pk).exists():
        movie.hate_users.remove(user)
        hate = False
    else:
        movie.hate_users.add(user)
        hate = True
    hate_status = {
        'hated': hate,
        'count': movie.hate_users.count(),
    }
    return JsonResponse(hate_status)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movie_favorite(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    user = request.user
    if movie.favorite_users.filter(pk=user.pk).exists():
        movie.favorite_users.remove(user)
        favorite = False
    else:
        movie.favorite_users.add(user)
        favorite = True
    favorite_status = {
        'favorited': favorite,
        'count': movie.favorite_users.count(),
    }
    return JsonResponse(favorite_status)






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
