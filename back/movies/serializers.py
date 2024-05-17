from rest_framework import serializers
from .models import Movie, Genre
from accounts.models import User

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class MovieListSerializer(serializers.ModelSerializer):
    class UserInfoSerializer(serializers.ModelSerializer):
        class Meta:
            model=User
            fields=('username',)
    user=UserInfoSerializer(read_only=True)
    class Meta:
        model = Movie
        fields = ('pk', 'title', 'overview','release_date','poster_path','vote_count','vote_average', 'user')

class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__'


class MovieReadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('tmdb_id', 'title', 'overview','release_date','poster_path','vote_count','vote_average','backdrop_path', 'adult', 'genres', 'popularity')
        # fields = '__all__'
