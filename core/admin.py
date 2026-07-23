from django.urls import path
from django.shortcuts import render, redirect
from django.contrib import admin, messages
from django import forms
import openpyxl
from .models import SiteSettings, RFQRequest, Inquiry, GalleryItem, Blog


class BlogAdminForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 28,
                'style': 'font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 13px;',
                'placeholder': (
                    '<h2>Section heading</h2>\n'
                    '<p>Paragraph text...</p>\n'
                    '<ul>\n  <li>Point one</li>\n  <li>Point two</li>\n</ul>'
                ),
            }),
        }


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

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'author')
    change_list_template = "admin/core/blog/change_list.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('upload-excel/', self.upload_excel, name='upload-excel'),
        ]
        return my_urls + urls

    def upload_excel(self, request):
        if request.method == "POST":
            excel_file = request.FILES.get("excel_file")
            if not excel_file or not excel_file.name.endswith('.xlsx'):
                self.message_user(request, "Please upload a valid .xlsx file.", level=messages.ERROR)
                return redirect("..")
            
            try:
                wb = openpyxl.load_workbook(excel_file)
                sheet = wb.active
                
                header_row = True
                created_count = 0
                for row in sheet.iter_rows(values_only=True):
                    if header_row:
                        header_row = False
                        continue
                        
                    title = row[0]
                    author = row[1] if len(row) > 1 and row[1] else "Admin"
                    content = row[2] if len(row) > 2 and row[2] else ""
                    
                    if title:
                        Blog.objects.create(title=title, author=author, content=content)
                        created_count += 1
                        
                self.message_user(request, f"Successfully imported {created_count} blogs.")
            except Exception as e:
                self.message_user(request, f"Error processing file: {e}", level=messages.ERROR)
                
            return redirect("..")
            
        return render(request, "admin/excel_upload.html")
