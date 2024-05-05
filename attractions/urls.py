from django.urls import path
from . import views

urlpatterns = [
    path('', views.attraction_list, name='attraction_list'),
    path('<int:pk>/', views.attraction_detail, name='attraction_detail'),
    # Add more URL patterns as needed
]
