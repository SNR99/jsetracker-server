
from rest_framework import serializers

from tracker.models import Stock


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = "__all__"

    time = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
