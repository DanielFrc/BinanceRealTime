from datetime import datetime
import json 
import logging 
import app_settings as constants

from util.GenerateApiRequest import GenerateApiRequest
from QueryProcessor.GetByQuoteAsset import GetByQuoteAsset



def main():
    #https://official-joke-api.appspot.com/random_joke -> for test
    #Getting the date for files
    date = datetime.now().strftime(constants.DATE_FOR_FILES)
    
    #Initialize Logging
    logging.basicConfig(filename=constants.LOG_FOLDER + 
                                 constants.LOG_NAME + 
                                 date + constants.LOG_EXTENSION,
                        level=logging.INFO,
                        format=constants.LOG_FORMAT,
                        encoding=constants.UTF8_ENCODING)

    ###https://datausa.io/api/data?drilldowns=Nation&measures=Population

    logging.info("Process started")

    get_usd_symbols = GetByQuoteAsset()

    symbols = get_usd_symbols.get_by_quote_asset("USDT")
    
    #symbols.to_csv("symbols2.csv",index=False,encoding="utf-8")

    api = GenerateApiRequest()

    for symbol in symbols["symbol"]:

        params = {
            "symbol"
        }


    
    logging.info("Process ended")


if __name__ == '__main__':
    main()