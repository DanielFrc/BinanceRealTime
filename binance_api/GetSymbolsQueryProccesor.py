from util.GenerateApiRequest import GenerateApiRequest
import app_settings as constants 
import logging 
import json
import pandas as pd

"""
Class to connect to Binance API to get Symbols dataset
"""

class GetSymbolsQueryProccesor:
    SYMBOLS_ENDPOINT = constants.BINANCE_API_BASE_URL + constants.BINANCE_API_EXCHANGE_INFO
    handle_request = ""

    def __init__(self):
        self.handle_request =  GenerateApiRequest()
    

    def get_symbols(self, dataframe=False):
        """
        Function to get symbols (cryptos) from Binance API
        Returns:
            symbols (dic): Dictionary with symbols
        """
        try:
            response = self.handle_request.generate_get_request(self.SYMBOLS_ENDPOINT)
            json_response = json.loads(response.text)

            symbols = json_response["symbols"]

            if dataframe :
                return self.convert_symbols_to_dataframe(symbols)

            return symbols
        
        except Exception as e:
            #Handling exception
            logging.exception("Error processing request")
    
    def convert_symbols_to_dataframe(self, symbols) :
        """
        Function to convert Symbols object to Datafame
        Rarameters:
            symbols (dic): Dictionary with symbols
        Returns:
            df (pandas.DataFrame): dataframe of symbols
        """
        try:
            df = pd.DataFrame(symbols)
            return df
        
        except Exception as e:
            #Handling exception
            logging.exception("Error processing request")

        