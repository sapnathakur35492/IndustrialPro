from django.db import models

class Capability(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    process_image = models.ImageField(upload_to='capabilities/')
    machinery_used = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Manufacturing Capabilities"

    def __str__(self):
        return self.title

class Infrastructure(models.Model):
    CATEGORY_CHOICES = [
        ('Factory', 'Factory Building'),
        ('Floor', 'Production Floor'),
        ('Machinery', 'Machinery'),
        ('Warehouse', 'Warehouse'),
        ('Lab', 'Quality Lab'),
        ('Testing', 'Testing Equipment'),
        ('Dispatch', 'Loading & Dispatch Area'),
    ]
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='infrastructure/')
    
    def __str__(self):
        return f"{self.title} ({self.get_category_display()})"

class Certification(models.Model):
    title = models.CharField(max_length=255)
    document = models.FileField(upload_to='certifications/')

    def __str__(self):
        return self.title

class ExportMarket(models.Model):
    country_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    flag_image = models.ImageField(upload_to='flags/', blank=True, null=True)

    def __str__(self):
        return self.country_name
