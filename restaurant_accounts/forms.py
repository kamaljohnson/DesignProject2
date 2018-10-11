from django import forms


class RestaurantForm(forms.Form):
    name = forms.CharField(label='name')
    city = forms.CharField()


class MenuForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    price = forms.FloatField()


class OfferForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
