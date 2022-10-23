from telnetlib import GA
from django.db import models
from .defines import DIRECTIONS,SHIPS, ROOMS, GAME_CONFIGURATION


class Ship(models.Model):
    """
    Model definition for a ship

    Args:
        models (Model): model django class instance
    """

    kind = models.CharField(choices=SHIPS, max_length=50)
    body_length = models.PositiveSmallIntegerField()
    head_position = models.CharField(max_length=10)
    direction = models.CharField(choices=DIRECTIONS ,max_length=1)
    
    @property
    def critical_points(self):
        #define segun kind
        pass


    class Meta:
        """Meta definition for Ship."""
      
        verbose_name = 'Ship'
        verbose_name_plural = 'Ships'

    def __str__(self):
        return f"{self.kind} / {self.body_length}"


class User(models.Model):
    """Model definition for User."""

    nick_name = models.CharField(max_length=50)
    token = models.CharField(max_length=20)

    class Meta:
        """Meta definition for User."""

        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        """Unicode representation of User."""
        pass


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
        """Unicode representation of Room."""
        pass

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
