from django.urls import path

from tracker.api.v2.views import *

urlpatterns = [
    path('', SomeStocksView),

]
