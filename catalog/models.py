from datetime import date

from django.db import models

NULLABLE = {'null': 'True', 'blank': 'True'}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    image = models.ImageField(upload_to='products/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='id категории')
    price = models.IntegerField(verbose_name='Цена', **NULLABLE)
    created_at = models.DateField(verbose_name='Дата создания', default=date.today())
    changed_at = models.DateField(verbose_name='Дата изменения', default=date.today())

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['category', 'name']


class CompanyContact(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    icon_bootstrap = models.CharField(max_length=100, verbose_name='Иконка Bootstrap')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class UserQuestion(models.Model):
    user_name = models.CharField(max_length=150, verbose_name='Имя')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Почта')
    question = models.TextField(verbose_name='Вопрос')
    created_at = models.DateField(verbose_name='Дата', default=date.today())

    def __str__(self):
        return f'{self.user_name}: {self.question[:20]}'

    class Meta:
        verbose_name = 'Вопрос пользователя'
        verbose_name_plural = 'Вопросы пользователей'
