from django.urls import path
from . import views

urlpatterns = [
    path('', views.user),
    path('<str:username>/', views.user_detail)
]



