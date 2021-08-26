import boto3
import json
import logging

# from boto3.exceptions


class KinesisProducer:
    """Producer class for aws kinesis streams

    This class will emit records with given key as partition key and given data as data.
    """

    KINESIS = "kinesis"

    def __init__(self, stream_name, key):
        self.STREAM_NAME = stream_name
        self.PARTITION_KEY = key
        self.kinesis_client = boto3.client(self.KINESIS)

        super().__init__()

    def put_record(self, record):
        """Put single record in the stream

        Parameters:
            data(dic): A dicctionary with raw data to put in kinesis.
        Response:
           bool: True if the record is received by kinesis, false if there
           was an exception while putting the records.
        """
        try:
            # Try to connect with kinesis and put the record u
            self.kinesis_client.put_record(
                StreamName=self.STREAM_NAME,
                Data=json.dumps(record),
                PartitionKey=self.PARTITION_KEY,
            )

            # Return true if the connection to kinesis not fails
            return True

        except Exception:
            # Handling exception if some error occurs while putting the
            # record.
            logging.exception(
                "Error sending data to {0} stream".format(self.STREAM_NAME)
            )

            # Return false if some error occurs
            return False

    def put_records(self, records):
        """Put a list of records in the stream
        Parameters:
            records(list): A dicctionary list with raw data to put in kinesis
        Response:
            response(bool): True if the record is received by kinesis, false if there was an exception while putting the records
        """
        try:

            for record in records:

                response = self.put_record(record)

                if response == False:
                    raise Exception("Records was not sended to Kinesis")

            return True
        except Exception:
            # Handling exception
            logging.exception(
                "Error sending data to {0} stream".format(self.STREAM_NAME)
            )
            return False
