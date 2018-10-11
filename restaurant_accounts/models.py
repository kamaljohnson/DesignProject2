from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from accounts.models import user_account


class Restaurant(models.Model):
    owner = models.ForeignKey(user_account, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    rating = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    city = models.CharField(max_length=255)

    def __str__(self):
        return self.name + " - " + str(self.owner)


class ItemType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Item(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    type = models.ForeignKey(ItemType, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    offer_price = models.IntegerField()  # can be used to display the offer price for the product
    rating = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return self.name + ' | ' + str(self.offer_price) + ' Rs | ' + str(
            self.price - self.offer_price) + ' Rs off |' + ' *' * self.rating


class OfferType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Offer(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    type = models.ForeignKey(OfferType, on_delete=models.CASCADE)
