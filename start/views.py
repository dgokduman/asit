from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Category
from django.shortcuts import redirect

def view_404(request, exception=None):
    # make a redirect to homepage
    # you can use the name of url or just the plain link
    return redirect('/') # or redirect('name-of-index-url')

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def chemicals(request):
    return render(request,"chemicals.html")

def team(request):
    return render(request,"team.html")

def contact(request):
    return render(request,"contact.html")

from django.shortcuts import render
from .models import Product

def products(request):
    query = request.GET.get('q', '')  # Arama terimi al
    category_id = request.GET.get('category', '')  # Kategori filtresi al

    # Filtreleme işlemi
    products = Product.objects.all()

    if query:
        products = products.filter(name__icontains=query)  # Arama terimine göre filtrele

    if category_id:
        products = products.filter(category_id=category_id)  # Kategoriye göre filtrele

    # Kategoriler, arama terimi ve ürünler gibi context verileri gönder
    categories = Category.objects.all()  # Kategorileri al
    return render(request, 'products.html', {
        'products': products,
        'categories': categories,
        'query': query,
    })

def products_by_category(request, category_id):
    products = Product.objects.filter(category_id=category_id)  # Kategoriyi filtrele
    categories = Category.objects.all()  # Kategorileri al
    return render(request, 'products.html', {'products': products, 'categories': categories})

def gallery(request):
    return render(request,"gallery.html")