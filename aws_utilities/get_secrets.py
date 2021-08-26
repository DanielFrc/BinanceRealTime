import boto3
import base64
import logging
import json


class GetSecrets:
    """Class to handle connection to AWS Secrets API

    Contains the method to get a secret, giving the secret name and the
    region where is stored.
    """

    # Initialize constants
    SERVICE_NAME = "secretsmanager"
    SECRET_STRING = "SecretString"
    SECRET_BINARY = "SecretBinary"

    def __init__(self, secret_name, region_name) -> None:
        self.secret_name = secret_name
        self.region_name = region_name

    def get_secret(self):
        """Get secret object from AWS.

        function to get secret from a especific region on aws.

            Parameters:
                secret_name(str):  Name of the secret in aws
                region_name(str): Region where the secret is stored
            Returns:
                Dict: object with the aws secret
        """

        # Create a Secrets Manager client
        session = boto3.session.Session()
        client = session.client(
            service_name=self.SERVICE_NAME, region_name=self.region_name
        )

        try:
            # Tries to get the secret
            get_secret_value_response = client.get_secret_value(
                SecretId=self.secret_name
            )

            # Parse the response. If the secret is an string, return a json
            # else return a decoded binary secret.
            if self.SECRET_STRING in get_secret_value_response:
                secret_json = get_secret_value_response[self.SECRET_STRING]
                return json.loads(secret_json)
            else:
                decoded_binary_secret = base64.b64decode(
                    get_secret_value_response[self.SECRET_BINARY]
                )
                return decoded_binary_secret

        except Exception:
            # Handle the exception if some error occurs during the execution
            # and store in the log.
            logging.exception("Error while retreaving the secret")
