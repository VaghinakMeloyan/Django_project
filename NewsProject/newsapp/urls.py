from django.urls import path
from .views import *

urlpatterns = [
    path('', CategoryListView.as_view(), name="category"),
    path('news/<slug:slug>/', CategoryDetailView.as_view(), name='news_detail')

]