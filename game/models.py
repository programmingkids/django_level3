from django.db import models
from django.core import validators

from .validates import check_name


# Create your models here.
class Monster ( models.Model ) :
    TYPE_CHOICES = (
        (1, "炎属性"),
        (2, "水属性"),
        (3, "闇属性"),
    )
    
    name = models.CharField(
        max_length=100
    )
    hp = models.IntegerField(
        default=0
    )
    mp = models.IntegerField(
        default=0
    )
    type = models.IntegerField(
        choices=TYPE_CHOICES
    )

    def __str__(self):
        s = "<Monster " +  \
            "ID=" + str(self.id) + " " +  \
            "名前=" + self.name + " " +  \
            "HP=" + str(self.hp) + " " + \
            "MP=" + str(self.mp) + " " + \
            "タイプ=" + self.get_type_display() + " " + \
            ">"
        return s


class Job( models.Model ):
    name = models.CharField(
        max_length=100
    )

    def __str__(self):
        s = "<Job " +  \
            "ID=" + str(self.id) + " " +  \
            "名前=" + self.name + " " +  \
            ">"
        return s


class Player( models.Model ):
    name = models.CharField(
        max_length=100
    )
    age = models.IntegerField(
        default=0
    )
    hp = models.IntegerField(
        default=0
    )
    mp = models.IntegerField(
        default=0
    )
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    def __str__(self):
        s = "<Player " +  \
            "ID=" + str(self.id) + " " +  \
            "名前=" + self.name + " " +  \
            "HP=" + str(self.hp) + " " + \
            "MP=" + str(self.mp) + " " + \
            "職業=" + self.job.name + " " + \
            ">"
        return s


class Character( models.Model ) :
    name = models.CharField(
        max_length=100
    )
    age = models.IntegerField()
    
    def __str__(self):
        s = "<Character " +  \
            "ID=" + str(self.id) + " " +  \
            "名前=" + self.name + " " +  \
            "年齢=" + str(self.age) + " " + \
            ">"
        return s


class Weapon( models.Model ) :
    name = models.CharField(
        max_length=100
    )
    attack = models.IntegerField()
    character = models.ManyToManyField(Character)

    def __str__(self):
        s = "<Weapon " +  \
            "ID=" + str(self.id) + " " +  \
            "名前=" + self.name + " " +  \
            "攻撃力=" + str(self.attack) + " " + \
            ">"
        return s


class User( models.Model ) :
    name = models.CharField(
        max_length=100,
        #validators=[
        #    check_name,
        #]
    )
    email = models.EmailField()
    age = models.IntegerField(
        default=0,
        #validators=[
        #    validators.MinValueValidator(10),
        #    validators.MaxValueValidator(20),
        #]
    )
    hobby = models.CharField(
        max_length=50
    )
    
    def __str__(self):
        s = "<User " +  \
            "ID=" + str(self.id) + " " +  \
            "名前=" + self.name + " " +  \
            "メール=" + self.email + " " +  \
            "年齢=" + str(self.age) + " " +  \
            "趣味=" + self.hobby + " " +  \
            ">"
        return s
