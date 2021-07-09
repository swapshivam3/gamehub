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
    description = models.TextField(null=True)
    name = models.TextField(null=False, default='SpaceWars')
    created_by = models.TextField(null=False, default='Admin')

    def _str_(self):
        return self.name
