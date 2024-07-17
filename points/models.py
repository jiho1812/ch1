from django.db import models

class UserProfile(models.Model):
    nickname = models.CharField(max_length=100, unique=True)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.nickname


# Create your models here.
