# Dependencies
import logging
import pandas as pd

# Internal packages
import app_settings as constants
from binance_api.generate_request_api import GenerateRequestApi
from query_processor.get_by_quote_asset import GetByQuoteAsset


class GetPricesBySymbol:
    def __init__(self):
        # Initializing objects
        self.get_by_quote_asset = GetByQuoteAsset()
        self.generate_request_api = GenerateRequestApi()

    def get_prices_by_symbol(self, symbol):
        """
        Function to get full information of a crypto with current price
        Rarameters:
            symbol(str): String with the symbol of the crypto
        Returns:
            df(pandas.DataFrame): dataframe with the full information
        """
        try:

            # Getting all the symbols of the given crypto
            symbols = self.get_by_quote_asset.get_by_quote_asset(symbol)

            # Getting the full price list at the moment
            prices_list = self.generate_request_api.generate_request(
                constants.BINANCE_API_PRICES, dataframe=True
            )

            # Getting book ticker
            book_ticker = self.generate_request_api.generate_request(
                constants.BINANCE_API_BOOK_TICKER, dataframe=True
            )

            # Getting 24hr ticker
            hr_ticker = self.generate_request_api.generate_request(
                constants.BINANCE_API_TICKER_24_HRS, dataframe=True
            )

            # Merging the dataframe
            df = pd.merge(symbols, prices_list, how="inner", on="symbol")
            df = pd.merge(df, book_ticker, how="inner", on="symbol")
            df = pd.merge(df, hr_ticker, how="inner", on="symbol")

            return df

        except Exception as e:
            # Handling exception
            logging.exception("Error merging the dataframe")
