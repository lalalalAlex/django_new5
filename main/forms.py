from .models import News, Comments
from django.forms import ModelForm, TextInput, Textarea


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ["title", "description"]
        widgets = {"title": TextInput(attrs={
            'class': 'rounded',
            'style': 'width: 610px; margin-left: 45px; margin-bottom: 4px; border-color: #E1E1E1; height: 50px; margin-top: 0;',
            'placeholder': 'Введите Название'
        }),
            "description": Textarea(attrs={
                'class': 'rounded',
                'style': 'width: 910px; margin-left: 45px; margin-bottom: 4px; border-color: #CFCFCF; height: 200px;',
                'placeholder': 'Введите Описание'
        })
                    }


class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = ["name", "description"]
        widgets = {"name": TextInput(attrs={
            'class': 'rounded',
            'style': 'width: 610px; margin-left: 45px; margin-bottom: 4px; border-color: #E1E1E1; height: 50px; margin-top: 0;',
            'placeholder': 'Введите Имя'
        }),
            "description": TextInput(attrs={
                'class': 'rounded',
                'style': 'width: 910px; margin-left: 45px; margin-bottom: 4px; border-color: #CFCFCF; height: 200px;',
                'placeholder': 'Введите Комментарий'
        })
                    }
