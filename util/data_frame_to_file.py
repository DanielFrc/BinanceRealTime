from datetime import datetime
import logging

import app_settings as constants


class DataFrameToFile:
    """Class to generate files from a dataframe

    Class to handle the creation of several files from dataframe
    """

    # Initialize date parameter
    date = ""

    def generate_csv(self, df, csv_name):
        """
        Generate a CSV file from a dataframe
            Parameters:
                df (pandas.DataFrame): The dataframe source for csv
                csv_name (str): Name of the CSV generated
        """

        try:
            # updating date parameter to concatenate in the name
            self.date = datetime.now().strftime(constants.DATE_FOR_FILES)

            # String with the full path of the csv, concatenates path,  name and extension
            full_name = (
                constants.CSV_FOLDER + csv_name + self.date + constants.CSV_EXTENSION
            )

            # Converting dataframe to csv with UTF-8 encoding and ignoring index
            df.to_csv(full_name, index=False, encoding=constants.UTF8_ENCODING)

        except Exception as e:
            # Handling exceptions
            logging.exception("Error ocurred generetating csv")

    def generate_parquet(self, df, parquet_name):
        """
        Generate parquet file from a dataframe
            Parameters:
                df (pandas.DataFrame): The dataframe source for csv (withot path and extension)
                parquet_name (str): Name of the CSV generated

        """
        try:
            # updating date parameter to concatenate in the name
            self.date = datetime.now().strftime(constants.DATE_FOR_FILES)

            # String with the full path of the parquet, concatenates path,  name and extension
            full_name = (
                constants.PARQUET_FOLDER
                + parquet_name
                + self.date
                + constants.PARQUET_EXTENSION
            )

            # Converting dataframe to csv with UTF-8 encoding, ignoring index and gzip compression
            df.to_parquet(
                full_name, index=False, compression=constants.GZIP_COMPRESSION
            )

        except Exception as e:
            # Handling exceptions
            logging.exception("Error ocurred generetating parquet file")

    def generate_json(self, df, json_name):
        """
        Generate json file from a dataframe
            Parameters:
                df (pandas.DataFrame): The dataframe source for csv (withot path and extension)
                json_name (str): Name of the generated JSON

        """
        try:
            # updating date parameter to concatenate in the name
            self.date = datetime.now().strftime(constants.DATE_FOR_FILES)

            # String with the full path of the parquet, concatenates path,  name and extension
            full_name = (
                constants.JSON_FOLDER + json_name + self.date + constants.JSON_EXTENSION
            )

            # Converting dataframe to json
            df.to_json(full_name, orient="records")

        except Exception as e:
            # Handling exceptions
            logging.exception("Error ocurred generetating parquet file")
