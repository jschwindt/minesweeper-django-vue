from rest_framework import serializers

from .models import Game
from .board import Board


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'status', 'created_at', 'started_at', 'time_taken',
                    'width', 'height', 'mines', 'board']

    def create(self, validated_data):
        player =  self.context['request'].user
        width = validated_data['width']
        height = validated_data['height']
        mines = validated_data['mines']
        board = Board(width, height, mines)
        game = Game(
            status = Game.NEW,
            player = player,
            width = width,
            height = height,
            mines = mines,
            board = board.cells
        )
        game.save()
        return game
