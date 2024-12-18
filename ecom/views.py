from django.shortcuts import render, redirect
from .models import Product

def home_view(request):
    return render(request, 'product_details/home.html')

def add_product(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        image = request.FILES.get('image')

        Product.objects.create(
            product_name=product_name,
            description=description,
            price=price,
            stock=stock,
            image=image
        )
        return redirect('home_view')

    return render(request, 'product_details/add_product.html')

def show_products(request):

    products = Product.objects.all()
    return render(request, 'product_details/show_product.html', {'products': products})
