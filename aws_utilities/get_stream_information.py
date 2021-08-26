from boto3 import client


class GetStreamInformation:
    KINESIS = "kinesis"

    def __init__(self, stream_name) -> None:
        self.stream_name = stream_name
        self.kinesis_client = client(self.KINESIS)

    def get_shards(self):

        response = self.kinesis_client.describe_stream(StreamName=self.stream_name)

        shards = response["StreamDescription"]["Shards"]

        return shards
