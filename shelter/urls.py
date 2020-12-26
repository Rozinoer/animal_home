from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'shelter'
urlpatterns = [
    path('main/', views.index, name='index'),
    path('search_pet/', views.search_page, name='search_page'),
    path('search_pet/filter', views.search_filter, name='search_filter'),
]