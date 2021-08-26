# Dependencies
import logging
from datetime import datetime
import time

# Internal Modules
import app_settings as constants
from QueryProcessor.echo_prices import EchoPrices
from aws_utilities.get_stream_information import GetStreamInformation


def main():
    # https://official-joke-api.appspot.com/random_joke -> for test
    # Getting the date for files
    date = datetime.now().strftime(constants.DATE_FOR_FILES)

    # Initialize Logging
    logging.basicConfig(
        filename=constants.LOG_FOLDER
        + "get_"
        + constants.LOG_NAME
        + date
        + constants.LOG_EXTENSION,
        level=logging.INFO,
        format=constants.LOG_FORMAT,
        encoding=constants.UTF8_ENCODING,
    )

    ###https://datausa.io/api/data?drilldowns=Nation&measures=Population

    logging.info("Process started")

    stream_info = GetStreamInformation(constants.AWS_KINESIS_STREAM)
    shards = stream_info.get_shards()

    # print(shards)

    for shard in shards:
        read_data = EchoPrices(
            constants.AWS_KINESIS_STREAM, shard["ShardId"], iterator_type="LATEST"
        )
        read_data.run()

    # self, stream_name, shard_id, iterator_type, worker_time=30, sleep_interval=0.5

    logging.info("Process ended")


if __name__ == "__main__":
    main()
