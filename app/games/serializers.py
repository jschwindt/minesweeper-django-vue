from datetime import datetime
from rest_framework import serializers

from .models import Game
from .board import Board


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'status', 'level', 'created_at', 'started_at', 'time_taken',
                    'width', 'height', 'mines', 'user_board', 'board_mines']

    def create(self, validated_data):
        player =  self.context['request'].user
        width = validated_data['width']
        height = validated_data['height']
        mines = validated_data['mines']
        level = validated_data['level']
        board = Board(width, height, mines)
        game = Game(
            status = Game.NEW,
            player = player,
            width = width,
            height = height,
            level = level,
            mines = mines,
            user_board = board.user_board,
            board_mines = board.board_mines,
        )
        game.save()
        return game

    def update(self, instance, validated_data):
        status = validated_data.get('status')
        if status == Game.PLAYING:
            instance.started_at = datetime.now()
        instance.status = status
        instance.user_board = validated_data.get('user_board')
        instance.time_taken = validated_data.get('time_taken')
        instance.save()
        return instance
