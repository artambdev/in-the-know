from . import views
from django.urls import path

urlpatterns = [
    path('', views.MainPage.as_view(), name='home'),
    path('<slug:slug>/', views.view_post, name='view_post'),
    path('create/', views.create_post, name='create_post'),
]