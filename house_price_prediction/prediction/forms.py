from django import forms

class HousePriceForm(forms.Form):
    Area = forms.FloatField(label='Enter the Area of house', widget=forms.NumberInput(attrs={
        'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
        'placeholder': 'Enter the Area of house'
    }))
    Room = forms.FloatField(label='Enter the number of rooms', widget=forms.NumberInput(attrs={
        'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
        'placeholder': 'Enter the number of rooms'
    }))
    Lon = forms.FloatField(label='Enter the Longitude', widget=forms.NumberInput(attrs={
        'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
        'placeholder': 'Enter the Longitude'
    }))
    Lat = forms.FloatField(label='Enter the Latitude', widget=forms.NumberInput(attrs={
        'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
        'placeholder': 'Enter the Latitude'
    }))
