from django.urls import path
from . import views
from .views import FetchMoviesAPIView

urlpatterns = [
    path('movies/', views.movie_list),
    path('movies/<int:movie_pk>/', views.movie_detail),
    path('fetch-movies/', FetchMoviesAPIView.as_view(), name='fetch-movies'),
]



