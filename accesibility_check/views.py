from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
# from .forms import LoanForm
from datetime import date, timedelta 
from django.utils import timezone
# Create your views here.


class HomeView(generic.TemplateView):
    template_name = 'accesibility_check/home.html'


def check_page(request):
    pass