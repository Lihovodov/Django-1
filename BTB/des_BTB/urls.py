from django.urls import path
from . import views

# app_name="des_BTB"
urlpatterns =[
	path('', views.price, name='home'),
	path('price',views.index, name='price'),
	path('create',views.create, name='create'),

]