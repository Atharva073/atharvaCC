from django.db import models

class Login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=100)
    def __str__(self):
        return self.username