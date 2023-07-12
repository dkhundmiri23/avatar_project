from django.db import models
from django.contrib.auth.models import User

class Nation(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Character(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='characters/')
    nation = models.ForeignKey(Nation, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

