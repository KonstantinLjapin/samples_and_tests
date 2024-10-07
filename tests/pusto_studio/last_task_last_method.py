import csv
from django.http import HttpResponse
from last_tast_model import PlayerLevel


def export_to_csv():
    """Выгрузка данных игрока в CSV."""
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="player_levels.csv"'

    writer = csv.writer(response)
    writer.writerow(['Player ID', 'Level Title', 'Is Completed', 'Received Prize'])

    player_levels = PlayerLevel.objects.get.select_related('player', 'level')

    for player_level in player_levels:
        level_prizes = player_level.level.levelprize_set.all()
        prize_titles = ', '.join(prize.prize.title for prize in level_prizes) if level_prizes.exists() else 'None'
        writer.writerow(
            [player_level.player.player_id, player_level.level.title, player_level.is_completed, prize_titles])

    return response
