from django.urls import path
from . import views

app_name = 'company'

urlpatterns = [
    path('capabilities/', views.capabilities, name='capabilities'),
    path('infrastructure/', views.infrastructure, name='infrastructure'),
    path('certifications/', views.certifications, name='certifications'),
    path('export-markets/', views.export_markets, name='export_markets'),
]
