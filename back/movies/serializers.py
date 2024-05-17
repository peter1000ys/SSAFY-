from rest_framework import serializers
from .models import Movie
from accounts.models import User


class MovieListSerializer(serializers.ModelSerializer):
    class UserInfoSerializer(serializers.ModelSerializer):
        class Meta:
            model=User
            fields=('username',)
    user=UserInfoSerializer(read_only=True)
    class Meta:
        model = Movie
        fields = ('pk', 'title', 'content', 'user')

class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields =('user',)
