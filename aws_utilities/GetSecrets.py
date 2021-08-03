import boto3
import base64
import logging
from botocore.exceptions import ClientError



"""
Class to handle connection to AWS Secrets API
"""
class GetSecrets: 

    SERVICE_NAME = "secretsmanager"
    SECRET_STRING = "SecretString"
    SECRET_BINARY = "SecretBinary"

    def get_secret(self, secret_name, region_name):
        """
        Function to get secret object from AWS
            Parameters:
                secret_name (str):  Name of the secret in aws
                region_name (str): Region where the secret is stored        
            Returns:
                secret_json: object with the aws secret
        """

        #Create a Secrets Manager client
        session = boto3.session.Session()

        client = session.client(
            service_name=self.SERVICE_NAME,
            region_name = region_name
        )

        try:
            get_secret_value_response = client.get_secret_value(
                SecretId=secret_name
            )

            if  self.SECRET_STRING in get_secret_value_response:
                secret_json = get_secret_value_response[self.SECRET_STRING]
                return secret_json
            else:
                decoded_binary_secret = base64.b64decode(get_secret_value_response[self.SECRET_BINARY])
                return decoded_binary_secret_json

        except Exception as e:
            #Handling exception
            logging.exception("Error while retreaving the secret")
        
        
 

