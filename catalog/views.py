import json

from django.shortcuts import render

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
    last_products = Product.objects.all().order_by('-id')[:5]
    print(last_products)

    return render(request, 'catalog/home.html', context={'data': data})


def contacts(request):
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
    return render(request, 'catalog/contacts.html', context={'cont': company_contacts})
