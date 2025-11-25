from django.urls import path
from . import views

"""urlpatterns = [
    path('req/', views.req_view),
    path('req/api/', views.api_view),
    path('style/', views.style_view),
    path('board/', views.board_main, name='board_main'),
    path('board/news/', views.board_news, name='board_news'),
    path('board/bullet/', views.board_bullet, name='board_bullet'),
    path('board/resp/', views.board_resp, name='board_resp'),
]"""

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('photo/<int:photo_id>/', views.photo_detail, name='photo_detail'),
    path('services/', views.services, name='services'),
    path('add-shooting-type/', views.add_shooting_type, name='add_shooting_type'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='portfolio/login.html'), name='login'),
    # НАША ПРОСТАЯ ФУНКЦИЯ ВЫХОДА
    path('logout/', views.custom_logout, name='logout'),
]