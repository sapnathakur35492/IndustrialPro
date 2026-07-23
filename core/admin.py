from django.urls import path
from django.shortcuts import render, redirect
from django.contrib import admin, messages
from django import forms
from django.utils.html import strip_tags, format_html
import openpyxl
from .models import SiteSettings, RFQRequest, Inquiry, GalleryItem, Blog


class TinyMCEWidget(forms.Textarea):
    """Admin WYSIWYG for blog HTML content (TinyMCE CDN — no extra pip package)."""

    def __init__(self, attrs=None):
        default = {
            'rows': 24,
            'class': 'blog-tinymce-editor vLargeTextField',
        }
        if attrs:
            default.update(attrs)
            if 'class' in attrs and 'blog-tinymce-editor' not in attrs.get('class', ''):
                default['class'] = f"blog-tinymce-editor {attrs['class']}"
        super().__init__(attrs=default)

    class Media:
        js = (
            'https://cdn.jsdelivr.net/npm/tinymce@6.8.2/tinymce.min.js',
            'admin/js/blog_tinymce_init.js',
        )


class BlogAdminForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'style': 'width: 100%; max-width: 720px;',
                'placeholder': 'Why Aluminium Castings Matter',
            }),
            'content': TinyMCEWidget(),
        }
        help_texts = {
            'title': 'Plain text only — do NOT put HTML tags (<h2>, etc.) in the title.',
            'content': (
                'Use the toolbar: Heading 2 / Heading 3 for sections, bold, lists, and links. '
                'Content is saved as HTML and styled on the website.'
            ),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title') or ''
        return strip_tags(title).strip()


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
    list_display = ('clean_title', 'author', 'created_at')
    search_fields = ('title', 'author')
    change_list_template = "admin/core/blog/change_list.html"
    fieldsets = (
        (None, {
            'fields': ('title', 'author', 'content'),
            'description': format_html(
                '<div style="padding:10px 12px;background:#fff7ed;border-left:4px solid #F97316;'
                'margin-bottom:12px;border-radius:4px;">'
                '<strong>How to write a blog:</strong><br>'
                '1. <strong>Title</strong> = plain text only (example: Why Aluminium Castings Matter)<br>'
                '2. <strong>Content</strong> = use the editor below. Select text → choose '
                '<em>Heading 2</em> / <em>Heading 3</em> for section titles. '
                'Do not put &lt;h2&gt; tags in the Title field.'
                '</div>'
            ),
        }),
    )

    @admin.display(description='Title', ordering='title')
    def clean_title(self, obj):
        return strip_tags(obj.title).strip()

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

                    title = strip_tags(str(row[0])).strip() if row[0] else ''
                    author = row[1] if len(row) > 1 and row[1] else "Admin"
                    content = row[2] if len(row) > 2 and row[2] else ""

                    if title:
                        Blog.objects.create(title=title, author=author, content=content or '')
                        created_count += 1

                self.message_user(request, f"Successfully imported {created_count} blogs.")
            except Exception as e:
                self.message_user(request, f"Error processing file: {e}", level=messages.ERROR)

            return redirect("..")

        return render(request, "admin/excel_upload.html")
