from django.urls import path
from . import views
from .views import FetchMoviesAPIView, FetchGenresAPIView

urlpatterns = [
    path('movies/', views.movie_list),
    path('movies/genres/', views.genre_list),
    path('movies/<int:movie_pk>/', views.movie_detail),
    path('fetch-movies/', FetchMoviesAPIView.as_view(), name='fetch-movies'),
    path('get-genres/', FetchGenresAPIView.as_view(), name='get-genres'),
    # path("filter-genre/", views.filter_genre, name="filter_genre"),
]



