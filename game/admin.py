from django.contrib import admin
from .models import User,  Ship,  Room, Game, Board, BoardShip, Shot

admin.site.register(User)
admin.site.register(Ship)
admin.site.register(Room)
admin.site.register(Game)
admin.site.register(Board)
admin.site.register(BoardShip)
admin.site.register(Shot)
