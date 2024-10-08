import csv
from django.http import HttpResponse
from last_tast_model import PlayerLevel


async def export_to_csv():
    """Выгрузка данных игрока в CSV."""
    with open('player_levels.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Player ID', 'Level Title', 'Is Completed', 'Received Prize'])
        player_levels = PlayerLevel.objects.all()
        for player_level in player_levels:
            level_prizes = player_level.level.levelprize_set.all()
            prize_titles = ', '.join(prize.prize.title for prize in level_prizes) if level_prizes.exists() else 'None'
            writer.writerow(
                [player_level.player.player_id, player_level.level.title, player_level.is_completed, prize_titles])

