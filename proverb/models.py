from django.db import models
from datetime import datetime

# Create your models here.
class Proverb(models.Model):
    content = models.CharField(max_length=250)
    meaning = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content + ' ' + self.meaning