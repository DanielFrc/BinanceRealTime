# Dependencies
import json
import logging

# Internal packages
from util.generate_api_request import GenerateApiRequest
from util.convert_to_dataframe import ConvertToDataframe
import app_settings as constants

"""
Class to generate request to Binance API
"""


class GenerateRequestApi:
    handle_request = None
    convert_to_dataframe = None

    def __init__(self):
        self.handle_request = GenerateApiRequest()
        self.convert_to_dataframe = ConvertToDataframe()

    def generate_request(self, url, dataframe=False, params=None):
        """
        Generate request to binanca API
        Returns:
            prices (dic): Dictionary with prices
        """
        try:
            # Generate url
            FULL_URL = constants.BINANCE_API_BASE_URL + url

            logging.info("Request to {0}".format(FULL_URL))

            response = self.handle_request.generate_get_request(FULL_URL, params)
            json_response = json.loads(response.text)

            if dataframe:
                return self.convert_to_dataframe.convert_json_to_dataframe(
                    json_response
                )

            return json_response

        except Exception as e:
            # Handling exception
            logging.exception("Error processing request")
