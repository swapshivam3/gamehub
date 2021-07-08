from django.contrib import admin
from .models import Game
# Register your models here.


class GameAdmin(admin.ModelAdmin):
    list = ('code', 'name', 'description')


admin.site.register(Game, GameAdmin)
