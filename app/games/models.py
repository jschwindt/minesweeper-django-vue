from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User


class Game(models.Model):
    NEW = 'new'
    PLAYING = 'play'
    PAUSED = 'pause'
    WON = 'won'
    LOST = 'lost'

    GAME_STATUS_CHOICES = [
        (NEW, 'new'),
        (PLAYING, 'playing'),
        (PAUSED, 'paused'),
        (WON, 'won'),
        (LOST, 'lost'),
    ]

    BEG = 'beg'
    INT = 'int'
    EXP = 'exp'
    CUS = 'cus'

    GAME_LEVEL_CHOICES = [
        (BEG, 'beginner'),
        (INT, 'intermediate'),
        (EXP, 'expert'),
        (CUS, 'custom'),
    ]
    status = models.CharField(max_length=6, choices=GAME_STATUS_CHOICES, default=NEW)
    level = models.CharField(max_length=3, choices=GAME_LEVEL_CHOICES, default=BEG)
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    started_at = models.DateTimeField(null=True, blank=True)
    time_taken = models.IntegerField(default=0)
    width = models.IntegerField(default=9)
    height = models.IntegerField(default=9)
    mines = models.IntegerField(default=10)
    user_board = JSONField(blank=True, default=dict)
    board_mines = JSONField(blank=True, default=dict)

    class Meta:
        ordering = ['-created_at']
