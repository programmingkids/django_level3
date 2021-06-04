from django.contrib import admin
from .models import Monster
from .models import Job
from .models import Player
from .models import Character
from .models import Weapon
from .models import User


# Register your models here.
admin.site.register(Monster)
admin.site.register(Job)
admin.site.register(Player)
admin.site.register(Character)
admin.site.register(Weapon)
admin.site.register(User)
