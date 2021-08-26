# External libraries
import logging
import json

# Internal packages
from util.generate_api_request import GenerateApiRequest
from util.convert_to_dataframe import ConvertToDataframe
import app_settings as constants


"""
Class to connect to Binance API to get Symbols dataset
"""


class GetSymbolsQueryProcessor:
    SYMBOLS_ENDPOINT = (
        constants.BINANCE_API_BASE_URL + constants.BINANCE_API_EXCHANGE_INFO
    )

    handle_request = ""
    convert_to_dataframe = ""

    def __init__(self):
        self.handle_request = GenerateApiRequest()
        self.convert_to_dataframe = ConvertToDataframe()

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

            if dataframe:
                return self.convert_to_dataframe.convert_json_to_dataframe(symbols)

            return symbols

        except Exception as e:
            # Handling exception
            logging.exception("Error processing request")
