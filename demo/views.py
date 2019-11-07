from django.shortcuts import render
from django.views.generic import (
    DetailView, RedirectView, UpdateView,TemplateView,DeleteView,
    ListView,CreateView)
from demo.models import Perro
# Create your views here.
class inicio(CreateView):
    model = Perro
    fields = ('nombre','raza','imagen')
    template_name = 'demo/index.html'
    def get_success_url(self):
        return ""