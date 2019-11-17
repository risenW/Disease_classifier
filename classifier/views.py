from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    return render(request, 'classifier/index.html')


def about(request):
    return render(request, 'classifier/about.html')

def predict(request):
    form = forms.ClassifierImage()
    return render(request, 'classifier/predict.html', {'form': form})