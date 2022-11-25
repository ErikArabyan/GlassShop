from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import sunglasses, aboutus, ourglasses
from random import sample, choice


class home(ListView):
    template_name = 'index.html'
    def get(self, request):
        items = sunglasses.objects.all()
        abo = aboutus.objects.all()
        orgl = ourglasses.objects.all()
        abo0 = [abo[0]]
        abo1 = [abo[1]]
        random_item = [items[0]]
        random_items = items[1:100]
        
        return render(request, self.template_name, 
        {'random_item':random_item, 'random_items':random_items, 'abo0':abo0, 'abo1':abo1, 'orgl':orgl})

class about(ListView):
    template_name = 'about.html'

    def get(self, request):
        abo = aboutus.objects.all()
        abo0 = [abo[0]]
        return render(request, self.template_name, {'abo0':abo0})

class shop(ListView):
    template_name = 'shop.html'

    def get(self, request):
        abo = aboutus.objects.all()
        abo1 = [abo[1]]
        return render(request, self.template_name, {'abo1':abo1})

class glasses(ListView):
    template_name = 'glasses.html'

    def get(self, request):
        orgl = ourglasses.objects.all()
        return render(request, self.template_name, {'orgl':orgl})