from django import forms
from geoposition.forms import GeopositionWidget, GeopositionField


class RestaurantForm(forms.Form):
    name = forms.CharField(label='name')
    position = GeopositionField(widget=GeopositionWidget)


class MenuForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    price = forms.FloatField()


class OfferForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
