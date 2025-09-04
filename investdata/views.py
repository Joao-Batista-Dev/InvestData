from django.views import View
from django.http import JsonResponse
from investdata.models import Stocks
from investdata.tasks import get_stock_price_task


class StockPriceView(View):
    def post(self, request):
        stock_name = request.POST.get('stock_name')

        if not stock_name:
            return JsonResponse({
                'menssage':'stock_name não informado'
            }, status=400)

        get_stock_price_task.delay(stock_name)

        return JsonResponse({
            'message': 'Tarefa disparada com sucesso!'
        })