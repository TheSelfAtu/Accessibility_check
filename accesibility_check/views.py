from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
# from .forms import LoanForm
from datetime import date, timedelta 
from django.utils import timezone
from .scripts.check_accesibility import alt_check
from .forms import URLForm
# Create your views here.


class HomeView(generic.TemplateView):
    template_name = 'accesibility_check/home.html'


def check_page(request):
    if request.method == "POST":
        form = URLForm(request.POST)
        form.is_valid()
        #     post = form.save(commit=False)
        #     post.author = request.user
        #     post.published_date = timezone.now()
        #     post.save()
        print(form.cleaned_data['url'])
        context = {'alt_check':alt_check(form.cleaned_data['url']),
                    'form':form,
                }
        return render(request,'accesibility_check/checked_result.html', context)
    else:
        form = URLForm()
        return render(request, 'accesibility_check/checked_result.html', {'form': form})