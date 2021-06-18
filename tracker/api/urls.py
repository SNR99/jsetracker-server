from django.urls import path

from .views import *

urlpatterns = [
    path('', StockAllView.as_view()),
    path('/<stock>', StockView.as_view()),

]
