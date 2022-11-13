from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import User, Ship, Room, Game, Board, BoardShip, Shot
from django.db.models import F


@receiver(post_save, sender=Shot)
def check_hit_to_ship(sender, instance, **kwargs):
    board = instance.board
    board_ships = board.board_ships.all()
    print(f"{board} BOARD")
    print(f"{board_ships} board_ships")
    try:
        board_ship = board_ships.get(coordinate=instance.coordinate)
        board_ship.ship_life = F('ship_life') - 1
        print("antes del save")
        board_ship.save(update_fields=['ship_life'])
        print("antes del except")
    except:
        print("no existe")
