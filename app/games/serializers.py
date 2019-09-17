from rest_framework import serializers
from .models import Game

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'status', 'created_at', 'started_at', 'time_taken',
                    'board_rows', 'board_cols', 'board_bombs', 'board']
