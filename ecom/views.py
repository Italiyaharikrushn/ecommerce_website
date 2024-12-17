from django.shortcuts import render, redirect
from .models import Product

def home_view(request):
    """
    View to render the home page.
    """
    return render(request, 'product_details/home.html')

def add_product(request):
    """
    View to handle the addition of a new product.
    If the request method is POST, it captures the form data, creates a new product,
    and redirects to the product listing page.
    Otherwise, it renders the add product form.
    """
    if request.method == 'POST':
        # Get data from form submission
        product_name = request.POST.get('product_name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        image = request.FILES.get('image')

        # Create a new product instance
        Product.objects.create(
            product_name=product_name,
            description=description,
            price=price,
            stock=stock,
            image=image
        )
        return redirect('show_products')  # Redirect to product listing

    return render(request, 'product_details/add_product.html')

def show_products(request):
    """
    View to display the list of products.
    Fetches all product entries from the database and renders them on the template.
    """
    products = Product.objects.all()  # Fetch all products
    return render(request, 'product_details/show_product.html', {'products': products})
