from django.shortcuts import render, redirect
from django.http import Http404,HttpResponseRedirect,HttpResponse
from .models import Article , Comment
from django.urls import reverse
from .forms import ArticleForm 

 

def price(request):
	article = Article.objects.order_by('-id')[:1]
	return render(request,'articles/price.html', {'title':'Главаная страница','article':article})

def index(request):
	return HttpResponse("<h4>Hello<h4>")

def create(request):
	error =''
	if request.method == "POST":
		form = ArticleForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
		else:
			error='Форма не корректна '
	form =ArticleForm() 
	context = {
		'form': form,
		'error': error
			
	}
	return render(request,'articles/create.html',context)


