from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView

from catalog.models import Category, Product, CompanyContact, UserQuestion


class ProductListView(ListView):
    model = Product

    def get_context_data(self):
        data = []
        categories = Category.objects.all()
        for category in categories:
            data.append({
                'category': category,
                'products': Product.objects.filter(category=category.pk)
            })
        data = sorted(data, key=lambda item: item['category'].pk)
        return {'data': data}


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'image', 'category', 'price']
    extra_context = {'categories': Category.objects.all()}

    def get_success_url(self):
        return reverse('catalog:view', kwargs={'pk': self.object.pk})


class UserQuestionCreateView(CreateView):
    model = UserQuestion
    fields = ['user_name', 'phone', 'email', 'question']
    company_contacts = CompanyContact.objects.all()
    company_contacts = sorted(company_contacts, key=lambda item: item.pk)
    extra_context = {'cont': company_contacts}
    success_url = reverse_lazy('catalog:contact')

