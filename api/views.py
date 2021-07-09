from django.shortcuts import render
from .serializers import GameSerializer
from rest_framework import generics, status
from rest_framework.views import APIView
from .models import Game
from rest_framework.response import Response

# Create your views here.


class GetGameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class CreateGame(generics.CreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class UpdateGame(generics.UpdateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GetGame(generics.RetrieveAPIView):
    queryset = Game.objects.all()  # currently ID Based
    serializer_class = GameSerializer
    # lookup_url_kwarg = 'code'

    # def get(self, request, format=None):
    #     code = request.GET.get(self.lookup_url_kwarg)
    #     if code != None:
    #         game = Game.objects.filter(code=code)
    #         if len(game) > 0:
    #             data = GameSerializer(game[0]).data
    #             data['is_host'] = self.request.session.session_key == game[0].host
    #             return Response(data, status=status.HTTP_200_OK)
    #         return Response({'Game Not Found': 'Invalid Game Code'}, status=status.HTTP_404_NOT_FOUND)

    #     return Response({'Bad Request': 'No Code Requested'}, status=status.HTTP_400_BAD_REQUEST)
