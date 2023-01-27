from .models import Reviews
from .models import AdditionalUsers
from django.forms import *


class ReviewsForm(ModelForm):
    class Meta:
        model = Reviews
        fields = ["text"]
        widgets = {"text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваш отзыв/рекомендацию'
            })
        }

    def __init__(self, *args, **kwargs):
        super(ReviewsForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'})


class AdditionalUsersForm(ModelForm):
    class Meta:
        model = AdditionalUsers
        fields = ['name_pol', 'mail', 'pas', 'id_dev']

        widgets = {
            "name_pol": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя пользователя/Название организации'
        }),
            "mail": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'you@example.com'
            }),
            "pas": TextInput(attrs={
                'class': 'form-control'
            }),
            "id_dev": NumberInput(attrs={
                'class': 'form-control'
            })
        }

    def __init__(self, *args, **kwargs):
        super(AdditionalUsersForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'})
