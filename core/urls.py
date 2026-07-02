from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact-rfq/', views.contact_rfq, name='contact_rfq'),
    path('gallery/', views.gallery, name='gallery'),
]
