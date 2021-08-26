# Dependencies
import json
import logging

# Internal packages
from util.GenerateApiRequest import GenerateApiRequest
from util.convert_to_dataframe import ConvertToDataframe
import app_settings as constants

"""
Class to get book ticker of all cryptos
"""


class Get24hTicker:
    PRICES_ENDPOINT = (
        constants.BINANCE_API_BASE_URL + constants.BINANCE_API_TICKER_24_HRS
    )
    handle_request = None
    convert_to_dataframe = None

    def __init__(self):
        self.handle_request = GenerateApiRequest()
        self.convert_to_dataframe = ConvertToDataframe()

    def get_24h_ticker(self, dataframe=False):
        """
        Function to get book ticker of (cryptos) from Binance API
        Returns:
            prices (dic): Dictionary with prices
        """
        try:
            response = self.handle_request.generate_get_request(self.PRICES_ENDPOINT)
            json_response = json.loads(response.text)

            if dataframe:
                return self.convert_to_dataframe.convert_json_to_dataframe(
                    json_response
                )

            return json_response

        except Exception as e:
            # Handling exception
            logging.exception("Error processing request")
