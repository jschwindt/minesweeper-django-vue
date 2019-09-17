from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import generics

from .models import Game
from .serializers import GameSerializer


@login_required
def index(request):
    return render(request, 'games/index.html')

class GameMixin:
    def get_queryset(self):
        current_user = self.request.user
        games = Game.objects.filter(player=current_user.id)
        return games

class GameList(GameMixin, generics.ListCreateAPIView):
    serializer_class = GameSerializer

class GameDetail(GameMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GameSerializer
