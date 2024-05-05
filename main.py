from dotenv import load_dotenv
load_dotenv()
import os
import requests
from datetime import datetime
import schedule
import time

def obtainDatas():
    formatted_date = datetime.now().strftime("%m/%d/%Y %H:%M:%S")

    valueFormatedBTC = getDatasBitcoin().replace(".", ",")
    valueFormatedETH = getDatasETH().replace(".", ",")
    valueFormatedDOGE = getDatasDoge().replace(".", ",")

    datas = {
        "Data_Bitcoin": formatted_date,
        "Valor_Bitcoin": valueFormatedBTC,
        "Data_Ethereum": formatted_date,
        "Valor_Ethereum": valueFormatedETH,
        "Data_Doge": formatted_date,
        "Valor_Doge": valueFormatedDOGE
    }
    return datas

def postDatasBitcoin():
    url = os.environ["URL_GOOGLE_SHEETS"]
    print("url:",url)
    response = requests.post(url, data=obtainDatas())

    if response.status_code != 200:
        print("Erro na requisição google sheets:", response.status_code)

def getDatasBitcoin():
    request = requests.get(f"https://api.mercadobitcoin.net/api/v4/tickers?symbols=BTC-BRL")
    return request.json()[0]["last"]

def getDatasETH():
    request = requests.get(f"https://api.mercadobitcoin.net/api/v4/tickers?symbols=ETH-BRL")
    return request.json()[0]["last"]

def getDatasDoge():
    request = requests.get(f"https://api.mercadobitcoin.net/api/v4/tickers?symbols=DOGE-BRL")
    return request.json()[0]["last"]

def main():
    postDatasBitcoin()

schedule.every().day.at("09:00").do(main)  
schedule.every().day.at("15:00").do(main)  
schedule.every().day.at("21:00").do(main)  


while True:
    schedule.run_pending()
    time.sleep(60) 