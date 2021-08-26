import logging

from binance_api.get_symbols_query_processor import GetSymbolsQueryProcessor
from datetime import datetime


"""
Class to obtain the list of USD Symbols
"""


class GetByQuoteAsset:
    get_symbols = None
    columns = [
        "symbol",
        "status",
        "baseAsset",
        "baseAssetPrecision",
        "quoteAsset",
        "quotePrecision",
        "quoteAssetPrecision",
        "baseCommissionPrecision",
        "quoteCommissionPrecision",
        "icebergAllowed",
        "ocoAllowed",
        "quoteOrderQtyMarketAllowed",
        "isSpotTradingAllowed",
        "isMarginTradingAllowed",
        "requestDate",
    ]

    def __init__(self):
        self.get_symbols = GetSymbolsQueryProcessor()

    def get_by_quote_asset(self, quote_asset):
        """
        Function to get only usd symbols, symbols to know the cryptos values in usd
        Parameters:
            quote_asset: The quote asset to get (i. e. USDT)
        Returns
            df(pandas.Dataframe): a DataFrame with symbols preprocessed, cleaned and filtered.

        """
        try:
            # Getting symbols in dataframe format
            symbols = self.get_symbols.get_symbols(dataframe=True)

            symbols["requestDate"] = datetime.now().isoformat()

            new_df = symbols[symbols["quoteAsset"] == quote_asset]

            return new_df[self.columns]

        except Exception as e:
            # Handling exception
            logging.exception("Error cleaning dataset")
