from django.forms import ModelForm , TextInput , Textarea
from .models import Article


class ArticleForm (ModelForm):
	class Meta:
		model = Article
		fields =["article_title", "article_text"]
		widgets ={
			"article_title": TextInput(attrs={
				'class': 'form-control',
				'placeholder':'Введите название'
			}),
			"article_text": Textarea(attrs={
				'class': 'form-control',
				'placeholder':'Введите описание'
			}),
		}