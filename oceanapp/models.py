from django.db import models

# Create your models here.
class Ocean(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Fish(models.Model):
    name = models.CharField(max_length=200)
    ocean = models.ForeignKey(Ocean, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class FishFact(models.Model):
    fact = models.CharField(max_length=200)
    fish = models.ForeignKey(Fish, on_delete=models.CASCADE)
    def __str__(self):
        return self.fact