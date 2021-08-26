import boto3
import logging
import time
from datetime import datetime, timedelta


class KinesisConsumer:
    """
    Generic consumer for Amazon Kinesis Streams
    """

    KINESIS = "kinesis"

    def __init__(
        self, stream_name, shard_id, iterator_type, worker_time=30, sleep_interval=0.5
    ):
        self.stream_name = stream_name
        self.shard_id = str(shard_id)
        self.iterator_type = iterator_type
        self.worker_time = worker_time
        self.sleep_interval = sleep_interval
        self.KINESIS_CLIENT = boto3.client(self.KINESIS)

    def process_records(self, records):
        """
        Generic function to implement the main logic of the consumer
        """
        raise NotImplementedError

    @staticmethod
    def iter_records(records):
        for record in records:
            part_key = record["PartitionKey"]
            data = record["Data"]
            yield part_key, data

    def run(self):
        next_iterator = self.__get_shard_iterator()
        start = datetime.now()
        finish = start + timedelta(seconds=self.worker_time)

        while finish > datetime.now():
            try:
                response = self.KINESIS_CLIENT.get_records(
                    ShardIterator=next_iterator, Limit=25
                )

                records = response["Records"]

                if records:
                    self.process_records(records)

                next_iterator = response["NextShardIterator"]

                time.sleep(self.sleep_interval)
            except Exception:
                logging.exception(
                    "Error getting records in the iterator: {0}".format(next_iterator)
                )
                time.sleep(1)
        return False

    def __get_shard_iterator(self):
        response = self.KINESIS_CLIENT.get_shard_iterator(
            StreamName=self.stream_name,
            ShardId=self.shard_id,
            ShardIteratorType=self.iterator_type,
        )
        return response["ShardIterator"]
