from django.db import models
from django.core.validators import FileExtensionValidator

class SiteSettings(models.Model):
    company_name = models.CharField(max_length=255, default="IndustrialPro")
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    about_text = models.TextField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return "Site Settings"

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SiteSettings, self).save(*args, **kwargs)

class RFQRequest(models.Model):
    name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    product_requirement = models.CharField(max_length=255)
    material_requirement = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField()
    file_upload = models.FileField(
        upload_to='rfq_files/', 
        blank=True, 
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'dwg', 'dxf', 'step', 'stp'])]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"RFQ from {self.company_name} - {self.name}"

class Inquiry(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Inquiries"
        ordering = ['-created_at']

    def __str__(self):
        return f"Inquiry from {self.name}"


class GalleryItem(models.Model):
    CATEGORY_CHOICES = [
        ('Factory', 'Factory'),
        ('Machinery', 'Machinery'),
        ('Castings', 'Castings'),
        ('Inspection', 'Inspection'),
        ('Video', 'Video'),
    ]

    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='gallery/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    video_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
