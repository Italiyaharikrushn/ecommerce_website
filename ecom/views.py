from django.shortcuts import render, redirect
from .models import Product, User
from django.contrib import messages
from .utils import never_cache_custom
from django.contrib.auth.hashers import make_password, check_password

def home_view(request):
    products = Product.objects.all()
    return render(request, 'product_details/home.html', {'products': products})

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

# This function handles the user register process
@never_cache_custom
def register(request):
    # if request.session.get('user_id'):
    #     return redirect('todo_list')

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = make_password(request.POST['password'])
        gender = request.POST['gender']
        age = request.POST['age']
        profession = request.POST['profession']

        if User.objects.filter(email=email).exists():
            messages.error(request, f"The email '{email}' is already registered. Please use a different email.")
            return render(request, 'base/register.html', {'name': name, 'phone': phone, 'gender': gender, 'age': age, 'profession': profession})

        User.objects.create(
            name=name, email=email, phone=phone, password=password,
            gender=gender, age=age, profession=profession
        )
        return redirect('login')

    return render(request, 'base/register.html')

# This function handles the user login process
@never_cache_custom
def login(request):
    # if request.session.get('user_id'):
    #     return redirect('todo_list')

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.get(email=email)
        if check_password(password, user.password):
            request.session['user_id'] = user.id
            request.session['user_name'] = user.name
            return redirect('todo_list')

    return render(request, 'base/login.html')
