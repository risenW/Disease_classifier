from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings

from .forms import ClassifierForm
from .models import Classifier
# Create your views here.

def index(request):
    return render(request, 'classifier/index.html')


def about(request):
    return render(request, 'classifier/about.html')

def predict(request):
    form = ClassifierForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        m = Classifier()
        m.image = form.cleaned_data['image']
        print(type(form.cleaned_data['image']))
        print("TYPE: " + form.cleaned_data['category'])
        m.save()
        
        return HttpResponseRedirect('/predict')

    return render(request, 'classifier/predict.html', {'form': form})

def upload_img(request):
    form = ClassifierForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        m = Classifier()
        m.image = form.cleaned_data['image']
        print(type(form.cleaned_data['image']))
        print("TYPE: " + form.cleaned_data['category'])
        m.save()
        
        return HttpResponseRedirect('/upload_img')

    return render(request, 'classifier/upload_img.html', {'form': form})
