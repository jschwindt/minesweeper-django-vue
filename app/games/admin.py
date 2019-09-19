from django.contrib import admin
from .models import Game

class GameAdmin(admin.ModelAdmin):
    list_display = ['started_at', 'status', 'level', 'player', 'time_taken',
                    'width', 'height', 'mines']
    ordering = ['-started_at']

admin.site.register(Game, GameAdmin)
