import logging
import pandas as pd
import sqlalchemy

from aws_utilities.get_secrets import GetSecrets
from db_handler.mapping.df_to_crypto_raw_map import DfToCryptoRawMap
from db_handler.models.crypto_raw import CryptoRaw


class CryptoRawQueryProcessor:
    ENGINE_STRING_BASE = "{0}+mariadbconnector://{1}:{2}@{3}:{4}/{5}"

    def __init__(self, aws_secret, aws_region, database) -> None:
        """ """

        # Create the mapping object: pandas.dataframe to CryptoRaw
        self.__df_crypto_raw_map = DfToCryptoRawMap()

        # Get the secrets of the database
        self.__secrets = GetSecrets(aws_secret, aws_region).get_secret()

        # Create sqlalchemy engine
        self.engine = sqlalchemy.create_engine(
            self.ENGINE_STRING_BASE.format(
                self.__secrets["engine"],
                self.__secrets["username"],
                self.__secrets["password"],
                self.__secrets["host"],
                self.__secrets["port"],
                database,
            )
        )

    def select_all(self):
        session = self.__get_session()
        return pd.read_sql(session.query(CryptoRaw).statement, session.bind)

    def select_by_asset(self, quote_asset):
        session = self.__get_session()
        return pd.read_sql(
            session.query(CryptoRaw).filter_by(tcr_quoteAsset=quote_asset).statement,
            session.bind,
        )

    def batch_insert(self, df, process_id):
        try:
            session = self.__get_session()
            session.add_all(
                self.__df_crypto_raw_map.create_list_from_df(df, process_id)
            )
            session.commit()

        except Exception:
            # Handle the exception if some error occurs during the execution
            # and store in the log.
            logging.exception("Error while parsing data")

    def single_insert(self, obj):
        try:
            session = self.__get_session()
            session.add(obj)
        except Exception:
            # Handle the exception if some error occurs during the execution
            # and store in the log.
            logging.exception("Error while parsing data")

    def __get_session(self):
        Session = sqlalchemy.orm.sessionmaker()
        Session.configure(bind=self.engine)
        return Session()
