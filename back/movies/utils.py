import requests
import json
from .models import Movie, Genre
from .serializers import MovieReadSerializer

token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5OTZjYzI3NTQ1MmIyOGE2NWQ1NmZkZTA5Njk0MWM4NCIsInN1YiI6IjY2M2Q4Y2UwMGYyYzdjMTlhNmM3NWI1ZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.2XhNWrsPvokdXhVEWX5ZHBctmKl7y5WckUfnppu6nIE"

def fetch_and_save_genres():
    url = "https://api.themoviedb.org/3/genre/movie/list?language=ko"

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers)
    response = json.loads(response.text)

    for results in response['genres']:
        Genre.objects.create(
            tmdb_id=results['id'],
            name=results['name'],
        )

def fetch_and_save_movies():
    for i in range(1, 101):
        url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=ko-KR&page={i}&sort_by=popularity.desc"

        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {token}"
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            movies_data = response.json().get('results', [])
            for movie_data in movies_data:
                movie_genre = movie_data['genre_ids']
                movie_rd = movie_data['release_date']
                if  movie_data['id'] == 699172:
                    continue
                if movie_data['id'] == 504903:
                    continue
                if not movie_data['genre_ids']:
                    continue
                if movie_data['release_date'] == "":
                    movie_rd = None
                elif int(movie_data['release_date'][:4]) <= 1980:
                    continue
                if movie_data['overview'] == "":
                    continue
                if Movie.objects.filter(pk=movie_data['id']):
                    continue
                movie_dict = {
                    'tmdb_id': movie_data['id'],
                    'title': movie_data['title'],
                    'overview': movie_data['overview'],
                    'release_date': movie_rd,
                    'poster_path': movie_data['poster_path'],
                    'vote_count':  movie_data['vote_count'],
                    'vote_average':  movie_data['vote_average'],
                    'popularity': movie_data['popularity'],
                    'backdrop_path': movie_data['backdrop_path'],
                    'adult': movie_data['adult'],
                    'genres': movie_genre,
                    'original_language': movie_data['original_language'],
                }
                serializer = MovieReadSerializer(data=movie_dict)
                if serializer.is_valid():
                    serializer.save()
                else:
                    print(serializer.errors)
        else:
            print('Failed to fetch data')

def get_movie_videos(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        return []

def delete_movies_without_trailers():
    movies = Movie.objects.all()
    for movie in movies:
        movie_id = movie.tmdb_id
        videos = get_movie_videos(movie_id)
        if not any(video['type'] == "Trailer" for video in videos):
            movie.delete()
            print(f"Deleted movie with ID: {movie_id} - {movie.title}")
# dumpdata 인코딩 문제 발생 시
# PYTHONIOENCODING=utf-8 python manage.py dumpdata --indent 4 movies.Movie > movies.json

