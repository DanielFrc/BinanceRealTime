from binance_api.GetSymbolsQueryProccesor import GetSymbolsQueryProccesor
from datetime import datetime
import logging 

"""
Class to obtain the list of USD Symbols
"""
class GetByQuoteAsset:
    get_symbols = ""
    columns = ["symbol",
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
               "requestDate"]

    def __init__(self):
        self.get_symbols = GetSymbolsQueryProccesor()

    def get_by_quote_asset(self,quote_asset):
        """
        Function to get only usd symbols, symbols to know the cryptos values in usd
        Parameters: 
            quote_asset: The quote asset to get (i. e. USDT)
        Returns
            df(pandas.Dataframe): a DataFrame with symbols preprocessed, cleaned and filtered.

        """
        try:

            symbols = self.get_symbols.get_symbols(dataframe = True)

            symbols["requestDate"] = datetime.now()

            new_df = symbols[symbols["quoteAsset"]==quote_asset]

            return new_df[self.columns]

        except Exception as e:
            #Handling exception
            logging.exception("Error cleaning dataset")