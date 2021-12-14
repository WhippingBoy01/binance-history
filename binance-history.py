#By WhippingBoy 2021
#Version 1.0

from binance import Client
import json
import time
from datetime import datetime


api_key = ""
api_secret = ""


client = Client(api_key, api_secret)

def Trades():
    pairs = client.get_exchange_info()

    for i in pairs['symbols']:
        
        orders = client.get_all_orders(symbol=i['symbol'], limit=100)

        if orders and orders[0]['status'] == "FILLED":
            Date = datetime.fromtimestamp(int(orders[0]['time'])/1000)
            #Buy orders
            if orders[0]['side'] == "BUY":
                print("Trade,",orders[0]['origQty'],",",i['baseAsset'],",,",orders[0]['cummulativeQuoteQty'],",",i['quoteAsset'],",,,,,Binance,",Date,",",orders[0]['orderId'],",")
            
            #Sell orders
            else:   
                print("Trade,",orders[0]['cummulativeQuoteQty'],",",i['quoteAsset'],",,",orders[0]['origQty'],",",i['baseAsset'],",,,,,Binance,",Date,",",orders[0]['orderId'],",")

            #ratelimit
        time.sleep(0.2)


def Deposits():
    #Fetch deposit history
    deposits = client.get_deposit_history()
    
    for i in deposits:
        Date = datetime.fromtimestamp(int(i['insertTime'])/1000)
        print("Deposit,",i['amount'],",",i['coin'],",,,,,,,,Binance,",Date,",")

def Withdraws():
    #Fetch withdraw history
    withdraws = client.get_withdraw_history()

    for i in withdraws:
        print("Withdrawal,,,,",i['amount'],",",i['coin'],",,,,,Binance,",i['applyTime'],",")

#Bittytax format
print("Type,Buy Quantity,Buy Asset,Buy Value in GBP,Sell Quantity,Sell Asset,Sell Value in GBP,Fee Quantity,Fee Asset,Fee Value in GBP,Wallet,Timestamp,Note")

Deposits()
Trades()
Withdraws()
