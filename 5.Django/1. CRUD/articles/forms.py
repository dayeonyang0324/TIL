from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    # title = forms.CharField(
    #     label='제목',
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'my-title form-control',
    #             'placeholder': 'Enter the Title',
    #             'maxlength': 10,
    #         }
    #     )
    # )
    # content = forms.CharField(
    #     label='내용',
    #     widget=forms.Textarea(
    #         attrs={
    #             'class': 'my-content form-control',
    #             'placeholder': 'Enter the Content',
    #             'rows': 5,
    #             'cols': 30,
    #         }
    #     ),
    #     error_messages={
    #         'required': '데이터를 입력해줄래...?',
    #     }
    # )


    class Meta:
        model = Article
        fields = ('title', 'content',)
        # fields = '__all__'
        # exclude = ('title',)