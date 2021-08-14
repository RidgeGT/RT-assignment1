from django.db import models
from django.utils import timezone

# Create your models here.
class Tile(models.Model):
    username = models.CharField(max_length=20)
    description = models.TextField()
    age = models.IntegerField()
    image = models.ImageField()
    date_created = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.username