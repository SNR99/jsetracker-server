from django.urls import path

from tracker.api.v1.views import *

urlpatterns = [
    path('', StockAllView.as_view()),
    path('<stock>', StockView.as_view()),

]
