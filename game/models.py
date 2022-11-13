from django.contrib.auth.models import AbstractUser
from django.db import models
from .defines import DIRECTIONS,SHIPS, ROOMS, GAME_CONFIGURATION


class Ship(models.Model):
    """
    Model definition for a ship

    Args:
        models (Model): model django class instance
    """

    kind = models.CharField(choices=SHIPS, max_length=50, unique=True)
    length = models.PositiveSmallIntegerField()

    @property
    def critical_points(self):
        #define segun kind
        pass


    class Meta:
        """Meta definition for Ship."""
      
        verbose_name = 'Ship'
        verbose_name_plural = 'Ships'

    def __str__(self):
        return f"{self.kind} / {self.length}"

class User(AbstractUser):
    """Model definition for User."""

    token = models.CharField(max_length=20)

    class Meta:
        """Meta definition for User."""

        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username


class Room(models.Model):
    """Model definition for Room."""

    kind = models.CharField(choices=ROOMS, max_length=6)
    active = models.BooleanField()
    code = models.CharField(max_length=6)
    password = models.CharField(null=True, blank=True, max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        """Meta definition for Room."""

        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'

    def __str__(self):
        return f"{self.kind} | {self.active} | {self.user}"

class Game(models.Model):
    """Model definition for Game."""

    players = models.CharField(max_length=250)  
    room = models.ForeignKey(
        Room, 
        on_delete=models.CASCADE,
        related_name="games")

    def game_configuration():
        return GAME_CONFIGURATION
    game_configuration = models.JSONField("GameConfiguration", default=game_configuration)

    class Meta:
        """Meta definition for Game."""

        verbose_name = 'Game'
        verbose_name_plural = 'Games'

    def __str__(self):
        """Unicode representation of Game."""
        return f"{self.room} - {self.players}"

class Board(models.Model):
    """Model definition for Board."""
    game = models.ForeignKey(
        Game, 
        on_delete=models.CASCADE,
        related_name="boards")

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="boards"
        )
    class Meta:
        """Meta definition for Board."""

        verbose_name = 'Board'
        verbose_name_plural = 'Boards'

    def __str__(self):
        return f"{self.game} - {self.user}"

class BoardShip(models.Model):
    """Model definition for BoardShip."""

    board = models.ForeignKey(
        Board, 
        on_delete=models.CASCADE,
        related_name="board_ships")
    
    ship = models.ForeignKey(
        Ship,
        on_delete=models.CASCADE,
        null=True)

    coordinate = models.CharField(max_length=50) 
    direction = models.CharField(choices=DIRECTIONS, max_length=1)
    ship_life = models.IntegerField()


    class Meta:
        """Meta definition for BoardShip."""

        verbose_name = 'BoardShip'
        verbose_name_plural = 'BoardShips'

    def __str__(self):
       return f"{self.board} - {self.ship}"

class Shot(models.Model):
    """Model definition for Shot."""

    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    coordinate = models.CharField(max_length=50)

    class Meta:
        """Meta definition for Shot."""

        verbose_name = 'Shot'
        verbose_name_plural = 'Shots'

    def __str__(self):
        """Unicode representation of Shot."""
        return f"{self.board.user.username}{self.coordinate}"
