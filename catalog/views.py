from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Category, Product, Industry
from core.forms import InquiryForm

def product_list(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    
    category_slug = request.GET.get('category')
    if category_slug:
        products = products.filter(category__slug=category_slug)
        
    context = {
        'categories': categories,
        'products': products,
        'current_category': category_slug
    }
    return render(request, 'catalog/product_list.html', context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save(commit=False)
            inquiry.product_name = product.name
            inquiry.save()
            messages.success(request, 'Your inquiry has been sent successfully.')
            return redirect('catalog:product_detail', slug=product.slug)
    else:
        form = InquiryForm(initial={'product_name': product.name})
        
    context = {
        'product': product,
        'form': form
    }
    return render(request, 'catalog/product_detail.html', context)

def industry_list(request):
    industries = Industry.objects.all()
    context = {'industries': industries}
    return render(request, 'catalog/industry_list.html', context)

def furnaces(request):
    return render(request, 'catalog/furnaces.html')

def foseco(request):
    return render(request, 'catalog/foseco.html')

def spares(request):
    return render(request, 'catalog/spares.html')

def gdc_machines(request):
    return render(request, 'catalog/gdc_machines.html')

def filters(request):
    return render(request, 'catalog/filters.html')

def thermol(request):
    return render(request, 'catalog/thermol.html')

def manufacturing(request):
    return render(request, 'catalog/manufacturing.html')
