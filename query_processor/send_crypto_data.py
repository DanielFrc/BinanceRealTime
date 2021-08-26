import logging
import threading
import time


from query_processor.get_prices_by_symbol import GetPricesBySymbol
from aws_utilities.kinesis_producer import KinesisProducer
from db_handler.crypto_raw_query_processor import CryptoRawQueryProcessor
import app_settings as constants


class SendCryptoData(threading.Thread):
    def __init__(self, symbol, sleep_interval=None):
        self.get_prices_by_symbol = GetPricesBySymbol()
        self.post_data_to_kinesis = KinesisProducer(
            constants.AWS_KINESIS_STREAM, symbol
        )
        self.SYMBOL = symbol
        self.SLEEP_INTERVAL = sleep_interval
        """
        To test
        """
        secret_name = "dev/appStream/MariaDb"
        region_name = "us-east-1"

        self.crypto_raw_handler = CryptoRawQueryProcessor(
            secret_name, region_name, "binanceapibd"
        )

        super().__init__()

    def send_to_datastream(self):
        """
        Get data by symbol and send to data stream
        """
        df = self.get_prices_by_symbol.get_prices_by_symbol(self.SYMBOL)
        self.crypto_raw_handler.batch_insert(df, "python-stream")
        # print(df.to_dict(orient="records"))
        # self.post_data_to_kinesis.put_records(df.to_dict(orient="records"))

    def run_continously(self):
        """Get crypto data at regular intervals"""
        while True:
            self.send_to_datastream()
            time.sleep(self.SLEEP_INTERVAL)

    def run(self):
        try:
            if self.SLEEP_INTERVAL:
                self.run_continously()
            else:
                self.send_to_datastream()
        except Exception:
            # Handling exception
            logging.exception(
                "Error getting data from {0} currency".format(self.SYMBOL)
            )
