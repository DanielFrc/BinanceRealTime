import logging
from aws_utilities.kinesis_consumer import KinesisConsumer


class SendToDatabase(KinesisConsumer):
    def process_records(self, records):
        """Print the partition key and data of each incoming record"""
        for part_key, data in self.iter_records(records):
            print("{0} : {1}".format(part_key, data))
