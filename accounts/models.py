from django.db import models


# Create your models here.

class user_account(models.Model):
    name = models.CharField(max_length=100)

    def create_user_account(self, name):
        self.name = name

    def __str__(self):
        return self.name
