from django.db import models

# Create your models here.
class Proverb(models.Model):
    name = models.CharField(max_length=250)
    meaning = models.CharField(max_length=250)

    def __str__(self):
        return self.meaning