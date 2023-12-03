from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *


class CategoryListView(ListView):
    model = Category
    template_name = 'index.html'
    context_object_name = "categories"


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'guard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.get_object().news.all() != None:
            context['news'] = self.get_object().news.all()

        return context


            # context['news_add'] = self.get_object().news_add.all()
            # return context