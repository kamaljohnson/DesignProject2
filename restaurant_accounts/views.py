from django.shortcuts import render
from .forms import RestaurantForm, MenuForm, OfferForm


def add_restaurant(request):
    form = RestaurantForm
    context = {'form': form}
    return render(request, 'restaurant_forms/restaurant_form.html', context)


def add_menu_item(request):
    form = MenuForm
    context = {'form': form}
    return render(request, 'restaurant_forms/menu_form.html', context)


def add_offer(request):
    form = OfferForm
    context = {'form': form}
    return render(request, 'restaurant_forms/offer_form.html', context)