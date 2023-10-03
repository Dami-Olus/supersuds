from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.home, name="homepage"),
    path('<int:question_id>/', views.detail, name="detail"),
    path('cars/', views.car_list, name="car_list"),
]