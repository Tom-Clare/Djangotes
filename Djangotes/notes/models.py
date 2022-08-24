from django.db import models

# Create your models here.

class User(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text
