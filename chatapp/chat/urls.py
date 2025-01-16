from django.urls import path
from .views import signup_view, login_view, chat_room, home_view
from . import views

urlpatterns = [
    path('', home_view, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('chat/', views.chat_room, name='chat_room'),
    path('<str:username>/', views.user_chat, name='user_chat'),  # User-specific chat
]
