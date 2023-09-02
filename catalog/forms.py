from django import forms

from catalog.models import Product, UserQuestion, Harvest
from const import FORBIDDEN_WORDS_IN_FORMS


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if isinstance(field.widget, forms.widgets.Textarea):
                field.widget.attrs['rows'] = 3
            if isinstance(field.widget, forms.widgets.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input m-2'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('created_at', 'changed_at', 'owner', )
        labels = {
            'name': 'Наименование',
            'description': 'Описание продукта',
            'image': 'Изображение продукта',
            'category': 'Категория',
            'price': 'Цена (₽/кг)',
        }

    def clean(self):
        cleaned_data = super().clean()
        name_description = cleaned_data.get('name') + cleaned_data.get('description')

        for word in FORBIDDEN_WORDS_IN_FORMS:
            if word in name_description:
                raise forms.ValidationError('В тексте не должно быть запрещенных слов')

        return cleaned_data


class UserQuestionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = UserQuestion
        exclude = ('created_at',)
        labels = {
            'user_name': 'Ваше имя',
            'phone': 'Телефон для связи',
            'email': 'Почта для связи',
            'question': 'Ваш вопрос',
        }

class HarvestForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Harvest
        fields = '__all__'

    def clean_is_current(self):
        cleaned_data = self.cleaned_data['is_current']

        print(len(self.cleaned_data['product'].harvest_set.filter(is_current=True)))
        if (cleaned_data):
            if len(self.cleaned_data['product'].harvest_set.filter(is_current=True)) > 0:
                raise forms.ValidationError('У продукта может быть только одна текущая поставка')

        return cleaned_data
