from util.GenerateApiRequest import GenerateApiRequest
import app_settings as constants 
import logging 
import json
import pandas as pd

class GetPricesQueryProccesor:
    PRICES_ENDPOINT = constants.BINANCE_API_BASE_URL + constants.BINANCE_API_PRICES
    handle_request = ""

    def __init__(self):
        self.handle_request =  GenerateApiRequest()

    def get_prices(self, dataframe=False):
        """
        Function to get prices of (cryptos) from Binance API
        Returns:
            prices (dic): Dictionary with prices
        """
        try:
            response = self.handle_request.generate_get_request(self.PRICES_ENDPOINT)
            json_response = json.loads(response.text)

            symbols = json_response["symbols"]

            if dataframe :
                return self.convert_symbols_to_dataframe(symbols)

            return symbols
        
        except Exception as e:
            #Handling exception
            logging.exception("Error processing request")

