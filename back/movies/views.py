from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from .serializers import MovieListSerializer, MovieSerializer
from .models import Movie

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
    