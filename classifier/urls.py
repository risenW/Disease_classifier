from django.conf.urls import url
from classifier import views

app_name = 'classifier'

urlpatterns= [
    url(r'^about/', views.about, name='about'),
    url(r'^upload_img/', views.upload_img, name='upload_img')
]