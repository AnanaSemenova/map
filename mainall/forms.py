from .models import Reviews
from django.forms import ModelForm, Textarea


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