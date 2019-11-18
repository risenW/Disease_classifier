from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
import os

from .forms import ClassifierForm
from .models import Classifier

#import for deep learning
# from keras.models import load_model
# from PIL import Image
# from PIL import Image
# import numpy as np
# import os
# import cv2

#Fixes the path error thrown by load model in keras==2.3.1
# import keras.backend.tensorflow_backend as tb
# tb._SYMBOLIC_SCOPE.value = True

# Path to input image
media_path = os.path.join(os.path.dirname(settings.BASE_DIR), 'media_cdn/images')

# Model names
pneumonia_model = './models/pneumonia_model.h5'
malaria_model = './models/malaria.h5'

# Create your views here.

def index(request):
    return render(request, 'classifier/index.html')


def about(request):
    return render(request, 'classifier/about.html')

def upload_img(request):
    form = ClassifierForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        m = Classifier()
        m.image = form.cleaned_data['image']
        print(type(form.cleaned_data['image']))
        print("TYPE: " + form.cleaned_data['category'])
        m.save()
        
        category = form.cleaned_data['category']
        return HttpResponseRedirect('/classifier/predict/?category=' + category)

    return render(request, 'classifier/upload_img.html', {'form': form})


def predict(request):
    # Preprocess image
    img_path = os.path.join(media_path, os.listdir(media_path)[0])
    # pnue_model = os.path.join(model_path, os.listdir(model_path)[0])

    category = request.GET.get('category')
    print("IMAGE PATH: " + img_path)
    print("CATEGORY: " + request.GET.get('category'))

    if category == 'MC':
        print("Classifier for malaria")

    else:
        #Predict for Pnuemonia
        img = preprocess_img(img_path)
        model = load_model(pneumonia_model)
        print("Making Predictions.....")
        score = model.predict(img)
        print("SCORE:" + str(score))

        label_indx = np.argmax(score)
        print("LABEL_INDEX: "+ str(label_indx))
        accuracy = np.max(score)

        label = get_label_name(label_indx)
        print("THE PREDICTED CLASS IS " + label + " WITH ACCURACY OF "+ str(accuracy))

        context = {
            'label': label,
            'accuracy': accuracy,
            'imagepath': img_path
        }

    return render(request, 'classifier/result.html', context)

def preprocess_img(img):
    img = cv2.imread(img)
    img = Image.fromarray(img, 'RGB')
    image = np.array(img.resize((150,150)))
    #process
    image = image/255
    final_img = []
    final_img.append(image)
    final_img = np.array(final_img)
    return final_img


def get_label_name(label):
    if label==0:
        return "NORMAL"
    if label==1:
        return "PNEUMONIA"


def clean_path(request):
    '''Cleans up image path'''
    # Delete image instance from model
    Classifier.objects.all().delete()

    # Delete image from media directory
    for img in os.listdir(media_path):
        os.remove(os.path.join(media_path, img))

    return HttpResponseRedirect('/')


