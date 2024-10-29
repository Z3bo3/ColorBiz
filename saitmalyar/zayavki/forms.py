from .models import Articles
from django.forms import ModelForm, TextInput, NumberInput, DateInput


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['name', 'phone']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                "placeholder": "Имя + Фамилия",
            }),
            "phone": NumberInput(attrs={
                'class': 'form-control',
                "placeholder": "Номер телефона",
            }),
        }