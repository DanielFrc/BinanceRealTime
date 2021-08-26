import pandas as pd
import logging


class ConvertToDataframe:
    def __init__(self) -> None:
        pass

    def convert_json_to_dataframe(self, json):
        """
        Function to convert json to Datafame
        Rarameters:
            json (list or dic): List or dictionary to convert to Dataframe
        Returns:
            df (pandas.DataFrame): dataframe with the result of the conversion
        """

        try:
            df = pd.DataFrame(json)
            return df

        except Exception as e:
            # Handling exception
            logging.exception("Error processing request")
