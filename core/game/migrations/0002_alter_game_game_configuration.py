# Generated by Django 3.2.16 on 2022-10-23 01:32

import core.game.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='game_configuration',
            field=models.JSONField(default=core.game.models.Game.game_configuration, verbose_name='GameConfiguration'),
        ),
    ]