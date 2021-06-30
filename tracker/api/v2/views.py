import json

from django.http import JsonResponse

from tracker.models import Stock


def SomeStocksView(request):
    received_json_data = json.loads(request.body.decode("utf-8"))
    stocks = list(received_json_data.values())[0]
    res = Stock.objects.filter(jse_code__in=stocks).values()

    return JsonResponse({
        "stocks": list(res)
    }, safe=False)


'''
def test(request):
    received_json_data = json.loads(request.body.decode("utf-8"))
    stocks = list(received_json_data.values())[0]
    res = Stock.objects.filter(jse_code__in=stocks).values()

    return JsonResponse({
        "stocks": list(res)
    }, safe=False)
'''
