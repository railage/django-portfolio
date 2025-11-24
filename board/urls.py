from django.urls import path
from board import views

app_name = 'board'

urlpatterns = [
    path('', views.index, name='index'),
    path('news/', views.news, name='news'),
    path('bullet/', views.bullet, name='bullet'),
    path('resp/', views.resp, name='resp'),
]