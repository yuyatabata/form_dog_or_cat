from django.db import models
from . import choice as ch

# Create your models here.
class Dogs_or_cats(models.Model):
    holiday = models.CharField(max_length=50, choices=ch.HOLIDAY)
    season = models.CharField(max_length=50, choices=ch.SEASON)
    travel = models.CharField(max_length=50, choices=ch.TRAVEL)
    work = models.CharField(max_length=50, choices=ch.WORK)
    mail = models.CharField(max_length=50, choices=ch.MAIL)

    def calculate_score(self):
        pass