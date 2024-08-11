from . import views
from django.urls import path

urlpatterns = [
    path('', views.MainPage.as_view(), name='home'),
    path('create/', views.create_post, name='create_post'),
    path('<slug:slug>/', views.view_post, name='view_post'),
]