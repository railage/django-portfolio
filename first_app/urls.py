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

urlpatterns = [
    path('', views.home, name='home'),
    path('photo/<int:photo_id>/', views.photo_detail, name='photo_detail'),
    path('services/', views.services, name='services'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('photo/<int:photo_id>/', views.photo_detail, name='photo_detail'),
    path('services/', views.services, name='services'),
    path('register/', views.register, name='register'),  # ← ДОБАВИЛИ
]