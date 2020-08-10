from . import views
from django.contrib import admin
from django.urls import path, include

app_name = 'accesibility_check'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('check_page', views.check_page, name='check_page'),

]