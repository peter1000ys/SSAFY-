from rest_framework import serializers
from .models import Review, Comment
from accounts.models import User


class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        # fields = '__all__'
        fields = ('id', 'movie_title', 'rank', 'content', 'user',)

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        fields = ('title', 'movie_title', 'rank', 'content', 'user',)
        read_only_fielsds = ('user',)

class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

# class ReviewSerializer(serializers.ModelSerializer):    
#     class Meta:
#         model = Review
#         fields = ('tmdb_id', 'title', 'overview','release_date','poster_path','vote_count','vote_average','backdrop_path', 'adult', 'genres', 'popularity')
        # fields = '__all__'
