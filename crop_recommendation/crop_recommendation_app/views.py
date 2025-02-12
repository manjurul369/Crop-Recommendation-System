from django.shortcuts import render

# Create your views here.
import pandas as pd
import joblib

def home(request):
    return render(request, 'home.html')

