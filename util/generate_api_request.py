import requests
import logging
from common.exceptions.get_request_exception import GetRequestException


class GenerateApiRequest:
    """Class to generate requests to a REST API

    Simple class to implement function to request information from and API
    """

    def generate_get_request(self, endpoint, parameters=None):
        """Send a get request to an Rest API
        Parameters:
            endpoint(str): String with url of the API endpoint
            parameters(List): List with the parameters to send in the request
        Return:
            json_response(str): String with the response of the get request
        """
        try:
            if parameters == None:
                response = requests.get(endpoint)
            else:
                response = requests.get(endpoint, params=parameters)

            if response.status_code != 200:
                raise GetRequestException

            return response
        except GetRequestException as e:
            # Handling exception
            logging.error(
                "Error with status code %d : %s ", response.status_code, response.text
            )
        except Exception as e:
            # Handling exception
            logging.exception("Error processing request")
