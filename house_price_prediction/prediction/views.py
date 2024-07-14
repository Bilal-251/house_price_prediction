from django.shortcuts import render
from . forms import HousePriceForm
import joblib
import pandas as pd


model = joblib.load('hpp_model.pkl')


def home(request):
    return render(request,'index.html')


def features(request):
    return render(request,'features.html')

def predict(request):
    if request.method == 'POST':
        form = HousePriceForm(request.POST)
        if form.is_valid():
            # Extract features from the form
            Area = form.cleaned_data['Area']
            Room = form.cleaned_data['Room']
            Lon = form.cleaned_data['Lon']
            Lat=form.cleaned_data['Lat']
            

            # DataFrame for prediction
            new_data = pd.DataFrame({
                'Area': [Area],
                'Room': [Room],
                'Lon': [Lon],
                'Lat': [Lat]
                
            })

            # Make prediction
            predicted_price = model.predict(new_data)[0]

            return render(request, 'result.html', {'predicted_price': predicted_price})
    else:
        form = HousePriceForm()

    return render(request, 'predict.html', {'form': form})