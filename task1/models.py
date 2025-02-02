from django.db import models


# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=20)
    balance = models.DecimalField(decimal_places=1, max_digits=6)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=40)
    cost = models.DecimalField(decimal_places=1, max_digits=6)
    size = models.DecimalField(decimal_places=1, max_digits=6)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name="games")

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} | {self.content}"
