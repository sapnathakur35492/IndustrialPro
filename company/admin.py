from django.contrib import admin
from .models import Capability, Infrastructure, Certification, ExportMarket

@admin.register(Capability)
class CapabilityAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Infrastructure)
class InfrastructureAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    list_filter = ('category',)

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(ExportMarket)
class ExportMarketAdmin(admin.ModelAdmin):
    list_display = ('country_name',)
