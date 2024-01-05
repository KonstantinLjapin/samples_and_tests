def warn_the_sheep(queue: list) -> str:
    sheep: str = "sheep"
    wolf: str = "wolf"
    warn_wolf: str = "Pls go away and stop eating my sheep"
    warn_sheep: str = "Oi! Sheep number {}! You are about to be eaten by a wolf!"
    if queue.index(wolf) == len(queue) - 1:
        return warn_wolf
    else:
        sheep_number: int = len(queue[queue.index(wolf)+1:])
        return warn_sheep.format(sheep_number)


print(warn_the_sheep(['sheep', 'sheep', 'wolf', 'sheep']))
