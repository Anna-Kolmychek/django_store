from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'message', 'preview')

    def get_success_url(self, *args, **kwargs):
        return reverse('blog:detail', args={self.object.pk})

    def form_valid(self, form):
        if form.is_valid:
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class BlogListView(ListView):
    model = Blog

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)
        queryset = queryset.order_by('-created_at', )
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()

        if self.object.views_count == 100:
            send_mail(
                '100 просмотров',
                f'Статья ({self.object.pk})"{self.object.title}" набрала 100 просмотров.',
                settings.EMAIL_HOST_USER,
                ['a.kolmychek@gmail.com']
            )
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'message', 'preview', 'is_published')
    success_url = reverse_lazy('blog:list')

    def get_success_url(self):
        return reverse('blog:detail', args=[self.kwargs['pk']])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')
