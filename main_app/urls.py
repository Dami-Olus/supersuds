from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.home, name="homepage"),
    path('cars/<int:car_id>/', views.detail, name="detail"),
    path('cars/', views.car_list, name="car_list"),
    path('cars/create/', views.CarCreate.as_view(), name='cars_create'),
    path('cars/<int:pk>/update', views.CarUpdate.as_view(), name='cars_update'),
    path('cars/<int:pk>/delete', views.CarDelete.as_view(), name='cars_delete'),
]