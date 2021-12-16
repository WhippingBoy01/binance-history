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

    for pair in pairs['symbols']:
        def gettrades():
            orders = client.get_all_orders(symbol=pair['symbol'], limit=100)
        
            if orders and orders[0]['status'] == "FILLED":
                for trade in orders:
                    Date = datetime.fromtimestamp(int(orders[0]['time'])/1000)

                    #Buy orders
                    if trade['side'] == "BUY":
                        print("Trade,",trade['origQty'],",",pair['baseAsset'],",,",trade['cummulativeQuoteQty'],",",pair['quoteAsset'],",,,,,Binance,",Date,",",trade['orderId'],",")
                    
                    #Sell orders
                    else:   
                        print("Trade,",trade['cummulativeQuoteQty'],",",pair['quoteAsset'],",,",trade['origQty'],",",pair['baseAsset'],",,,,,Binance,",Date,",",trade['orderId'],",")
        
        #Binace API ratelimit workaround
        try: 
            gettrades()

        except:
            time.sleep(30)
            gettrades()

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
