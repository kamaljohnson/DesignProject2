from django.contrib import admin
from .models import Restaurant, ItemType, Item, OfferType, Offer

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(ItemType)
admin.site.register(Item)

admin.site.register(OfferType)
admin.site.register(Offer)

