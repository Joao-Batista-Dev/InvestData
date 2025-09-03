from django.views import View
from django.http import response
from django.http import JsonResponse
from investdata.models import Stocks
from investdata.tasks import get_stock_price


class StockPriceView(View):
    def post(self, request):
        stock_name = request.POST.get('stock_name')

        get_stock_price.delay(stock_name)

        return JsonResponse(
            data={
                'message': 'Tarefa disparada com sucesso!'
            },
            status=200,
        )