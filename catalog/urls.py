from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('products/<slug:slug>/', views.product_detail, name='product_detail'),
    path('industries/', views.industry_list, name='industry_list'),
    path('furnaces/', views.furnaces, name='furnaces'),
    path('foseco/', views.foseco, name='foseco'),
    path('spares/', views.spares, name='spares'),
    path('gdc-machines/', views.gdc_machines, name='gdc_machines'),
    path('filters/', views.filters, name='filters'),
    path('thermol/', views.thermol, name='thermol'),
    path('manufacturing/', views.manufacturing, name='manufacturing'),
]
