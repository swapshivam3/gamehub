from django.db import models
import string
import random
# Create your models here.


def generate_unique_code():
    length = 6
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Game.objects.filter(code=code).count() == 0:
            break
    return code


class Game(models.Model):
    code = models.CharField(
        max_length=6, default=generate_unique_code, unique=True)
    description = models.CharField(max_length=200, null=True)
    name = models.CharField(null=False, max_length=50, default='SpaceWars')

    def _str_(self):
        return self.name
