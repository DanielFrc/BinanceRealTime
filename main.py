# Dependencies
import logging
from datetime import datetime

# Internal Modules
import app_settings as constants
from db_handler.crypto_raw_query_processor import CryptoRawQueryProcessor
from query_processor.send_crypto_data import SendCryptoData
from aws_utilities.get_secrets import GetSecrets

from util.data_frame_to_file import DataFrameToFile


def main():
    # https://official-joke-api.appspot.com/random_joke -> for test
    # Getting the date for files
    date = datetime.now().strftime(constants.DATE_FOR_FILES)

    # Initialize Logging
    logging.basicConfig(
        filename=constants.LOG_FOLDER
        + constants.LOG_NAME
        + date
        + constants.LOG_EXTENSION,
        level=logging.INFO,
        format=constants.LOG_FORMAT,
        encoding=constants.UTF8_ENCODING,
    )

    ###https://datausa.io/api/data?drilldowns=Nation&measures=Population

    logging.info("Process started")

    secret_name = "dev/appStream/MariaDb"
    region_name = "us-east-1"
    database = "binanceapibd"

    crypto_raw_qp = CryptoRawQueryProcessor(secret_name, region_name, database)
    df_to_file = DataFrameToFile()

    df = crypto_raw_qp.select_all()

    df_to_file.generate_csv(df, "binance_raw")

    df_to_file.generate_parquet(df, "binance_raw")

    df_to_file.generate_json(df, "binance_raw")

    # send_usdt_data = SendCryptoData("USDT", 60)
    # send_eth_data = SendCryptoData("ETH", 60)
    # send_btc_data = SendCryptoData("BTC", 60)

    # send_usdt_data.start()
    # send_eth_data.start()
    # send_btc_data.start()

    logging.info("Process ended")


if __name__ == "__main__":
    main()
