from django.conf.urls import url
from classifier import views

app_name = 'classifier'

urlpatterns= [
    url(r'^about/', views.about, name='about'),
    url(r'^predict/', views.predict, name='predict')
]