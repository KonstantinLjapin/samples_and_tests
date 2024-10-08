from last_tast_model import Player, Level, Prize, LevelPrize, PlayerLevel
from django.utils import timezone


def awarding_the_price(player_level: PlayerLevel) -> None:
    if player_level.completed:
        player = player_level.player
        level = player_level.level
        prize = Prize(title="YOU Awesome prize")# какакаято логика создания модели Prize
        prize.save()
        LevelPrize.objects.create(level=level, prize=prize, received=timezone.now())
        print(f"Prize '{prize.title}' has been assigned to player '{player.player_id}' for level '{level.title}'.")
    else:
        print(f"Player has not completed level")
