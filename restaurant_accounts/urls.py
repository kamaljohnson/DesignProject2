from django.contrib import admin
from django.urls import path, include

from .views import add_restaurant, add_menu_item, add_offer

urlpatterns = [
    path('add/restaurant/', add_restaurant, name='add_restaurant'),
    path('add/menu_item/', add_menu_item, name='add_menu_item'),
    path('add/offer/', add_offer, name='add_offer'),
]
