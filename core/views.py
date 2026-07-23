from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import SiteSettings, GalleryItem, Blog
from .forms import RFQForm, InquiryForm
from catalog.models import Category, Product, Industry
from company.models import Capability, Infrastructure, Certification, ExportMarket

def get_site_settings():
    return SiteSettings.objects.first()

def home(request):
    settings = get_site_settings()
    categories = Category.objects.all()
    capabilities = Capability.objects.all()
    industries = Industry.objects.all()
    featured_products = Product.objects.all()
    infrastructure_items = Infrastructure.objects.all()
    certifications = Certification.objects.all()
    export_markets = ExportMarket.objects.all()
    gallery_items = GalleryItem.objects.all()
    gallery_categories = GalleryItem.objects.values_list('category', flat=True).distinct()
    
    if request.method == 'POST' and 'rfq_submit' in request.POST:
        form = RFQForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your RFQ has been submitted successfully. We will get back to you shortly.')
            return redirect('core:home')
        else:
            messages.error(request, 'There was an error in your submission. Please check the form.')
    else:
        form = RFQForm()
    
    context = {
        'settings': settings,
        'categories': categories,
        'capabilities': capabilities,
        'industries': industries,
        'featured_products': featured_products,
        'infrastructure_items': infrastructure_items,
        'certifications': certifications,
        'export_markets': export_markets,
        'gallery_items': gallery_items,
        'gallery_categories': gallery_categories,
        'form': form,
    }
    return render(request, 'core/home.html', context)

def about(request):
    settings = get_site_settings()
    context = {'settings': settings}
    return render(request, 'core/about.html', context)

def contact_rfq(request):
    settings = get_site_settings()
    if request.method == 'POST':
        form = RFQForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your RFQ has been submitted successfully. We will get back to you shortly.')
            return redirect('core:contact_rfq')
        else:
            messages.error(request, 'There was an error in your submission. Please check the form.')
    else:
        form = RFQForm()

    context = {
        'settings': settings,
        'form': form,
    }
    return render(request, 'core/contact.html', context)


def gallery(request):
    settings = get_site_settings()
    gallery_items = GalleryItem.objects.all()
    categories = list(GalleryItem.objects.values_list('category', flat=True).distinct())

    # Fallback to Casting Photos when admin gallery is empty
    static_gallery = []
    if not gallery_items.exists():
        from django.templatetags.static import static
        titles = [
            'Casting Overview', 'Precision Parts', 'Aluminium Components', 'Finished Castings',
            'Machined Parts', 'Wheel Casting', 'Coupling Assembly', 'Industrial Handwheel',
            'Valve Handwheel', 'Pulley Casting', 'Export Batch', 'Quality Inspection',
            'Foundry Output', 'Die Cast Product', 'Component Set', 'GDC Casting',
            'Machined Coupling', 'Handwheel Range', 'Wheel Family', 'Product Showcase',
            'Aluminium Handwheels', 'Drive Pulleys', 'Cast Handwheels', 'Handwheel Set',
            'Wheel Collection', 'Aluminium Couplings', 'Flange Couplings', 'Shaft Couplings',
            'Coupling Detail', 'Precision Coupling', 'Coupling Finish',
        ]
        for i, title in enumerate(titles, 1):
            category = 'Castings'
            if i >= 21 and i <= 25:
                category = 'Castings'
            static_gallery.append({
                'title': title,
                'category': category,
                'image_url': static(f'images/castings/cast_{i:02d}.jpg'),
                'video_url': '',
            })
        categories = ['Castings']

    context = {
        'settings': settings,
        'gallery_items': gallery_items,
        'static_gallery': static_gallery,
        'categories': categories,
    }
    return render(request, 'core/gallery.html', context)


def facility(request):
    settings = get_site_settings()
    context = {
        'settings': settings,
    }
    return render(request, 'core/facility.html', context)

def blog_list(request):
    settings = get_site_settings()
    blogs = Blog.objects.all()
    context = {
        'settings': settings,
        'blogs': blogs,
    }
    return render(request, 'core/blog_list.html', context)

def blog_detail(request, pk):
    settings = get_site_settings()
    blog = get_object_or_404(Blog, pk=pk)
    related = Blog.objects.exclude(pk=blog.pk)[:3]
    context = {
        'settings': settings,
        'blog': blog,
        'related_blogs': related,
    }
    return render(request, 'core/blog_detail.html', context)
