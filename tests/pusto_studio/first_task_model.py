from django.db import models


class Player(models.Model):
    bio = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=25, unique=True)
    first_in = models.DateTimeField(auto_now_add=True)
    last_in = models.DateTimeField()
    entrance_points = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "player"
        verbose_name_plural = "players"
        get_latest_in = "last_in"

    def __str__(self):
        return self.nick_name


class TypeBoost(models.Model):
    description = models.CharField(max_length=100)
    short_description = models.CharField(max_length=25)
    effect = models.CharField(max_length=25)
    negative_effect = models.BooleanField(default=False)

    class Meta:
        verbose_name = "type_boost"
        verbose_name_plural = "types_boost"

    def __str__(self):
        return self.short_description


class Boost(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    typeboost = models.ForeignKey(TypeBoost, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "boost"
        verbose_name_plural = "boost"

    def __str__(self):
        return self.typeboost

