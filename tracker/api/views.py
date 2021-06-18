from django.http.response import HttpResponse, JsonResponse
from rest_framework import generics

import json
from tracker.models import Stock
from .serializers import StockSerializer

from rest_framework.views import APIView


class StockAllView(generics.ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class StockView(generics.ListAPIView):
    serializer_class = StockSerializer

    def get_queryset(self):
        stock = self.kwargs['stock']
        return Stock.objects.filter(jse_code=stock)


def test(request):

    received_json_data = json.loads(request.body.decode("utf-8"))
    stocks = eval(received_json_data)[0]["stock"]
    res = Stock.objects.filter(jse_code__in=stocks).values()

    return JsonResponse({
        "stocks": list(res)
    }, safe=False)
