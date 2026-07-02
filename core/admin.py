from django.contrib import admin
from .models import SiteSettings, RFQRequest, Inquiry, GalleryItem

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    pass

@admin.register(RFQRequest)
class RFQRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'company_name', 'email', 'country', 'created_at')
    search_fields = ('name', 'company_name', 'email')
    list_filter = ('created_at', 'country')

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'product_name', 'created_at')
    search_fields = ('name', 'email', 'product_name')
    list_filter = ('created_at',)


@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    search_fields = ('title',)
    list_filter = ('category', 'created_at')
