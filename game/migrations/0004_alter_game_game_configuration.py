# Generated by Django 4.1 on 2022-10-23 02:25

from django.db import migrations, models
import game.models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_alter_game_game_configuration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='game_configuration',
            field=models.JSONField(default=game.models.Game.game_configuration, verbose_name='GameConfiguration'),
        ),
    ]
