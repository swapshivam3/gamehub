from .views import GetGameList, GetGame, CreateGame
from django.urls import path, include

urlpatterns = [
    path('get-game-list', GetGameList.as_view()),
    path('get-game/<int:pk>', GetGame.as_view()),
    path('create-game', CreateGame.as_view()),
]
