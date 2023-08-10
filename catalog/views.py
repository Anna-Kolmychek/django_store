import json
from datetime import date

from django.shortcuts import render, redirect
from django.urls import reverse

from catalog.forms import NewProductForm
from catalog.models import Category, Product, CompanyContact


def home(request):
    data = []
    categories = Category.objects.all()
    for category in categories:
        data.append({
            'category': category,
            'products': Product.objects.filter(category=category.pk)
        })
    data = sorted(data, key=lambda item: item['category'].pk)

    # для доп. задания: добавьте выборку последних 5 товаров и вывод их в консоль.
    # last_products = Product.objects.all().order_by('-id')[:5]
    # print(last_products)

    return render(request, 'catalog/index.html', context={'data': data})


def contact(request):
    if request.method == 'POST':
        user_name = request.POST.get('name')
        user_phone = request.POST.get('phone')
        user_email = request.POST.get('email')
        user_message = request.POST.get('message')
        print(f'New message from: '
              f'{user_name} (phone: {user_phone}, email: {user_email})\n'
              f'message: {user_message}')

    company_contacts = CompanyContact.objects.all()
    company_contacts = sorted(company_contacts, key=lambda item: item.pk)
    return render(request, 'catalog/contact.html', context={'cont': company_contacts})


def product(request, product_id: int):
    context = {
        'product': Product.objects.filter(pk=product_id).select_related('category').get()
    }
    print(context)
    return render(request, 'catalog/product.html', context)


def new_product(request):
    if request.method == 'POST':
        form = NewProductForm(request.POST, request.FILES)
        prod = form.save()
        return redirect(f'../product/{prod.pk}')

    context = {
        'categories': Category.objects.all(),
    }
    return render(request, 'catalog/new_product.html', context)


def get_product_data(request):
    product_data = {
        'name': request.POST.get('name'),
        'description': request.POST.get('description'),
        'image': request.POST.get('image'),
        'category': request.POST.get('category'),
        'price': request.POST.get('price'),
        'created_at': date.today(),
        'changed_at': date.today(),
    }
    return product_data

def save_new_product(product_data):
    category = Category.objects.get(pk=product_data['category'])
    try:
        price = int(product_data['price'])
    except ValueError:
        price = None

    Product.objects.create(
        name=product_data['name'],
        description=product_data['description'],
        image=product_data['image'],
        category=category,
        price=price,
        created_at=product_data['created_at'],
        changed_at=product_data['changed_at'],
    )
