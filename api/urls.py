from .views import GetGameList, GetGame
from django.urls import path, include

urlpatterns = [
    path('get-game-list', GetGameList.as_view()),
    path('get-game', GetGame.as_view()),
]
