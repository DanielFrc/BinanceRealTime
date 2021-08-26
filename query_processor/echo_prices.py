import logging
from aws_utilities.kinesis_consumer import KinesisConsumer


class EchoPrices(KinesisConsumer):
    """Consumer that echo received data to standard output"""

    def process_records(self, records):
        """Print the partition key and data of each incoming record"""
        logging.info(records)
        for part_key, data in self.iter_records(records):
            print("{0} : {1}".format(part_key, data))
