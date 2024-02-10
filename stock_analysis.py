import requests
from datetime import datetime, timedelta
import pandas as pd
from io import StringIO

def pull_data(date, symbol):
    # GET current data
    url = f"https://api.polygon.io/v1/open-close/{symbol}/{date}?adjusted=true&apiKey=Nmwol_1RTDh7PMgtXViUZ63qBFppUY_c"
    response = requests.get(url)
    cur_data = response.json()

    while(cur_data['status'] == 'NOT_FOUND'):
        date = date - timedelta(days=1)
        url = f"https://api.polygon.io/v1/open-close/{symbol}/{date}?adjusted=true&apiKey=Nmwol_1RTDh7PMgtXViUZ63qBFppUY_c"
        response = requests.get(url)
        cur_data = response.json()
    
    # GET previous data (1 week)
    date = date - timedelta(days=7)
    url = f"https://api.polygon.io/v1/open-close/{symbol}/{date}?adjusted=true&apiKey=Nmwol_1RTDh7PMgtXViUZ63qBFppUY_c"
    response = requests.get(url)
    prev_data = response.json()
    
    # calculate data
    # if all the high-high, low-low, open-open, close-close is positive, then stock is increasing, highly reccomend to buy
    # if the open-open OR close-close is negative, do not recomend to buy right now bc stock is decreasing
    # if the high-high AND low-low is BOTH negative or positive then state the stock is volatile
    # if all the high-high, low-low, open-open, close-close is negative, then stock is decreasing, highly reccomend to sell
    return [prev_data, cur_data]


while(True):
    # Get the most recent date 
    current_date = datetime.now().date() - timedelta(days=1)
    symbol = input("Enter symbol: ")
    pull_data(current_date, symbol)


