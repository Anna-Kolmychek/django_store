from django.shortcuts import render


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        user_name = request.POST.get('name')
        user_phone = request.POST.get('phone')
        user_email = request.POST.get('email')
        user_message = request.POST.get('message')
        print(f'New message from: '
              f'{user_name} (phone: {user_phone}, email: {user_email})\n'
              f'message: {user_message}')

    return render(request, 'catalog/contacts.html')

