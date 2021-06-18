from django.urls import path

from .views import *

urlpatterns = [
    path('', StockAllView.as_view()),
    path('get/<stock>', StockView.as_view()),
    path('get/', test)

]
