import requests
from movies.models import Movie
token = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5OTZjYzI3NTQ1MmIyOGE2NWQ1NmZkZTA5Njk0MWM4NCIsInN1YiI6IjY2M2Q4Y2UwMGYyYzdjMTlhNmM3NWI1ZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.2XhNWrsPvokdXhVEWX5ZHBctmKl7y5WckUfnppu6nIE'
def get_movies_related(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/recommendations?language=ko-KR&page=1"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        recommended_movies = response.json().get('results', [])
        
        # 영화 ID 리스트 추출
        recommended_movie_ids = [movie['id'] for movie in recommended_movies]
        
        # 데이터베이스에 존재하는 영화 ID 리스트 추출
        existing_movie_ids = Movie.objects.filter(tmdb_id__in=recommended_movie_ids).values_list('tmdb_id', flat=True)
        
        # 데이터베이스에 없는 영화 제거
        filtered_movies = [movie for movie in recommended_movies if movie['id'] in existing_movie_ids]
        
        return filtered_movies
    else:
        return []


get_movies_related(823464)