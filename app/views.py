from django.shortcuts import render
import joblib
import pandas as pd

# Create your views here.
def index(request):
    return render(request, 'index.html')

def predict(request):
    return render(request, 'predict.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def process(request):
    loaded_model = joblib.load("./data/Crop_recommendation_model.joblib")
    sample_data = pd.DataFrame({
        'n': [request.GET['N']],
        'p': [request.GET['P']],
        'k': [request.GET['K']],
        'temp': [request.GET['temp']],
        'humidity': [request.GET['humidity']],
        'pH': [request.GET['pH']],
        'rainfall': [request.GET['rainfall']]
    })
    prediction = loaded_model.predict(sample_data)[0]
    data = {
        'final':prediction
    }
    return render(request, 'process.html', data)