from django.shortcuts import render
from .models import Capability, Infrastructure, Certification, ExportMarket

def capabilities(request):
    capabilities_list = Capability.objects.all()
    context = {'capabilities': capabilities_list}
    return render(request, 'company/capabilities.html', context)

def infrastructure(request):
    items = Infrastructure.objects.all()
    context = {'items': items}
    return render(request, 'company/infrastructure.html', context)

def certifications(request):
    certs = Certification.objects.all()
    context = {'certifications': certs}
    return render(request, 'company/certifications.html', context)

def export_markets(request):
    markets = ExportMarket.objects.all()
    context = {'markets': markets}
    return render(request, 'company/export_markets.html', context)
