from rest_framework import generics

from tracker.models import Stock
from ..serializers import StockSerializer


class StockAllView(generics.ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class StockView(generics.ListAPIView):
    serializer_class = StockSerializer

    def get_queryset(self):
        stock = self.kwargs['stock']
        return Stock.objects.filter(jse_code=stock)
