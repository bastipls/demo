from django.shortcuts import render
from django.views.generic import (
    DetailView, RedirectView, UpdateView,TemplateView,DeleteView,
    ListView,CreateView)
# Create your views here.
class inicio(TemplateView):
    template_name = 'demo/index.html'