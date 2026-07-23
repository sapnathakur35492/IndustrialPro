from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact-rfq/', views.contact_rfq, name='contact_rfq'),
    path('gallery/', views.gallery, name='gallery'),
    path('facility/', views.facility, name='facility'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
]
