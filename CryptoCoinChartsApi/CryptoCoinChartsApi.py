'''
Created on 24.01.2014

@author: Dirk Rother
@contact: dirrot@web.de
@license: GPL
@version: 0.1

'''

import requests
from Models import Coin, TradingPair

class API(object):
    '''
    This class is a wrapper class for the CryptoCoinCharts api.
    '''
    
    API_PATH = "http://api.cryptocoincharts.info/"
        
    def listcoins(self):
        '''
        Use this function to list all coins with their data which are available on cryptocoincharts.
        Usage: http://www.cryptocoincharts.info/v2/api/listCoins
        '''
        url = self.API_PATH + 'listCoins'
        
        json_data = requests.get(url).json()
        
        coins = []
        for entry in json_data:
            coin = Coin()
            coin.id = entry['id']
            coin.name = entry['name']
            coin.website = entry['website']
            coin.price_btc = entry['price_btc']
            coin.volume_btc = entry['volume_btc']
            coins.append(coin)
        
        return coins
    
    def tradingpair(self, pair):
        '''
        Use this function to query price and volume data for ONE trading pair.
        A list with all coin currencies can be found by using the listcoins method.
        A example pair: currency1_currency2 = "doge_btc" 
        Usage: http://www.cryptocoincharts.info/v2/api/tradingPair/[currency1_currency2]
        '''
        url = self.API_PATH + 'tradingPair/' + pair
        
        json_data = requests.get(url).json()
        
        tradingpair = TradingPair()
        tradingpair.id = json_data['id']
        tradingpair.price = json_data['price']
        tradingpair.price_before_24h = json_data['price_before_24h']
        tradingpair.volume_first = json_data['volume_first']
        tradingpair.volume_second = json_data['volume_second']
        tradingpair.volume_btc = json_data['volume_btc']
        tradingpair.best_market = json_data['best_market']
        tradingpair.latest_trade = json_data['latest_trade']

        return tradingpair
    
    def tradingpairs(self, pairs):
        '''
        Use this function to query price and volume data for MANY trading pairs.
        Usage: http://www.cryptocoincharts.info/v2/api/tradingPairs/[currency1_currency2,currency2_currency3,...]
               A example pair: currency1_currency2 = "doge_btc"
                               currency2_currency3 = "btc_eur"
               http://www.cryptocoincharts.info/v2/api/tradingPairs/"doge_btc,btc_eur"            
        '''
        url = self.API_PATH + 'tradingPairs/'
        data = { 'pairs':pairs }
        
	json_data = requests.get(url, params=data).json()
        
        tradingpairs = []
        for entry in json_data:
            tradingpair = TradingPair()
            tradingpair.id = entry['id']
            tradingpair.price = entry['price']
            tradingpair.price_before_24h = entry['price_before_24h']
            tradingpair.volume_first = entry['volume_first']
            tradingpair.volume_second = entry['volume_second']
            tradingpair.volume_btc = entry['volume_btc']
            tradingpair.best_market = entry['best_market']
            tradingpair.latest_trade = entry['latest_trade']
            tradingpairs.append(tradingpair)
        
        return tradingpairs
    
    def listofpairs(self):
        pass
    
