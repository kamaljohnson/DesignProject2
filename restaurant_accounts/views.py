from django.http import HttpResponse
from django.shortcuts import render
from .forms import RestaurantForm, MenuForm, OfferForm
from .models import Restaurant, Item, OfferType
from accounts.models import user_account


def add_restaurant(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            print("VALID")
            name = form.cleaned_data['name']
            city = form.cleaned_data['city']

            new_restaurant = Restaurant(
                owner=user_account.objects.get(name=request.user.username),  # need to be changed with the actual owner
                name=name,
                rating=0,
                city=city,
            )
            new_restaurant.save()

    form = RestaurantForm
    context = {'form': form}
    return render(request, 'restaurant_forms/restaurant_form.html', context)


def add_menu_item(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)

        if form.is_valid():
            print("VALID")
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']

            new_menu_item = Item(
                name=name,
                description=description,
                price=price,
            )

            new_menu_item.save()
    form = MenuForm
    context = {'form': form}
    return render(request, 'restaurant_forms/menu_form.html', context)


def add_offer(request):
    if request.method == 'POST':
        form = OfferForm(request.POST)

        if form.is_valid():
            print("VALID")
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']

            new_offer = OfferType(
                name=name,
                description=description,
            )
            new_offer.save()
    form = OfferForm
    context = {'form': form}
    return render(request, 'restaurant_forms/offer_form.html', context)
