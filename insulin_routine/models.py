from django.db import models
# Create your models here.
class Routine(models.Model):
    name = models.CharField(max_length=200)
    peso = models.IntegerField()
    old = models.IntegerField()
    disease = models.CharField(max_length=3)

    def __str__(self) -> str:
        return self.name

# Create your models here.
