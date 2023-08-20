from django.db import models

NULLABLE = {'blank': 'True', 'null': 'True'}


class Blog(models.Model):
    title = models.CharField(max_length=150, unique=True, verbose_name='заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug')
    message = models.TextField(verbose_name='содержимое', **NULLABLE)
    preview = models.ImageField(upload_to='blog/', verbose_name='превью', **NULLABLE)
    created_at = models.DateField(auto_now_add=True, verbose_name='дата создания')
    is_published = models.BooleanField(default=True, verbose_name='опубликовано (да/нет)')
    views_count = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
