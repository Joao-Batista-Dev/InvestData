from celery import shared_task
from investdata.models import Stocks
import yfinance as yf

@shared_task
def get_stock_price_task(stock_name):
    stock = yf.Ticker(stock_name + ".SA")
    price = stock.history(period="1d")["Close"].iloc[-1]
    
    Stocks.objects.create(
        name=stock_name, 
        price=float(price)
    )

    return float(price)
