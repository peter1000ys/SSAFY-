import requests
from .models import Movie
from .serializers import MovieReadSerializer

def fetch_and_save_movies():
    for i in range(1, 250):
        url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page={i}&sort_by=popularity.desc"

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5OTZjYzI3NTQ1MmIyOGE2NWQ1NmZkZTA5Njk0MWM4NCIsInN1YiI6IjY2M2Q4Y2UwMGYyYzdjMTlhNmM3NWI1ZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.2XhNWrsPvokdXhVEWX5ZHBctmKl7y5WckUfnppu6nIE"
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            movies_data = response.json().get('results', [])
            for movie_data in movies_data:
                movie_dict = {
                    'title': movie_data['title'],
                    'overview': movie_data['overview'],
                    'release_date': movie_data['release_date'],
                    'poster_path': movie_data['poster_path'],
                    'vote_count':  movie_data['vote_count'],
                    'vote_average':  movie_data['vote_average'],
                    'backdrop_path':movie_data['backdrop_path'],
                    'adult':movie_data['adult'],
                    'genres':movie_data['genre_ids'],
                }
                serializer = MovieReadSerializer(data=movie_dict)
                if serializer.is_valid():
                    serializer.save()
                else:
                    print(serializer.errors)
        else:
            print('Failed to fetch data')


