import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class CryptoRaw(Base):
    __tablename__ = "bin_tbl_crypto_raw"
    tcr_record_id = sqlalchemy.Column(sqlalchemy.BigInteger, primary_key=True)
    tcr_symbol_name = sqlalchemy.Column(sqlalchemy.String(length=100))
    tcr_status = sqlalchemy.Column(sqlalchemy.String(length=50))
    tcr_baseAsset = sqlalchemy.Column(sqlalchemy.String(length=50))
    tcr_baseAssetPrecision = sqlalchemy.Column(sqlalchemy.Integer)
    tcr_quoteAsset = sqlalchemy.Column(sqlalchemy.String(length=50))
    tcr_quotePrecision = sqlalchemy.Column(sqlalchemy.Integer)
    tcr_quoteAssetPrecision = sqlalchemy.Column(sqlalchemy.Integer)
    tcr_baseCommissionPrecision = sqlalchemy.Column(sqlalchemy.Integer)
    tcr_quoteCommissionPrecision = sqlalchemy.Column(sqlalchemy.Integer)
    tcr_icebergAllowed = sqlalchemy.Column(sqlalchemy.Boolean, default=True)
    tcr_ocoAllowed = sqlalchemy.Column(sqlalchemy.Boolean, default=True)
    tcr_quoteOrderQtyMarketAllowed = sqlalchemy.Column(sqlalchemy.Boolean, default=True)
    tcr_isSpotTradingAllowed = sqlalchemy.Column(sqlalchemy.Boolean, default=True)
    tcr_isMarginTradingAllowed = sqlalchemy.Column(sqlalchemy.Boolean, default=True)
    tcr_requestDate = sqlalchemy.Column(sqlalchemy.DateTime)
    tcr_price = sqlalchemy.Column(sqlalchemy.Float)
    tcr_bidPrice_x = sqlalchemy.Column(sqlalchemy.Float)
    tcr_bidQty_x = sqlalchemy.Column(sqlalchemy.Float)
    tcr_askPrice_x = sqlalchemy.Column(sqlalchemy.Float)
    tcr_askQty_x = sqlalchemy.Column(sqlalchemy.Float)
    tcr_priceChange = sqlalchemy.Column(sqlalchemy.Float)
    tcr_priceChangePercent = sqlalchemy.Column(sqlalchemy.Float)
    tcr_weightedAvgPrice = sqlalchemy.Column(sqlalchemy.Float)
    tcr_prevClosePrice = sqlalchemy.Column(sqlalchemy.Float)
    tcr_lastPrice = sqlalchemy.Column(sqlalchemy.Float)
    tcr_lastQty = sqlalchemy.Column(sqlalchemy.Float)
    tcr_bidPrice_y = sqlalchemy.Column(sqlalchemy.Float)
    tcr_bidQty_y = sqlalchemy.Column(sqlalchemy.Float)
    tcr_askPrice_y = sqlalchemy.Column(sqlalchemy.Float)
    tcr_askQty_y = sqlalchemy.Column(sqlalchemy.Float)
    tcr_openPrice = sqlalchemy.Column(sqlalchemy.Float)
    tcr_highPrice = sqlalchemy.Column(sqlalchemy.Float)
    tcr_lowPrice = sqlalchemy.Column(sqlalchemy.Float)
    tcr_volume = sqlalchemy.Column(sqlalchemy.Float)
    tcr_quoteVolume = sqlalchemy.Column(sqlalchemy.Float)
    tcr_openTime = sqlalchemy.Column(sqlalchemy.Float)
    tcr_closeTime = sqlalchemy.Column(sqlalchemy.Float)
    tcr_firstId = sqlalchemy.Column(sqlalchemy.Float)
    tcr_lastId = sqlalchemy.Column(sqlalchemy.Float)
    tcr_count = sqlalchemy.Column(sqlalchemy.Float)
    tcr_procces_id = sqlalchemy.Column(sqlalchemy.String(length=100))
    # tcr_process_date = sqlalchemy.Column(sqlalchemy.DateTime)
    # tcr_update_date = sqlalchemy.Column(sqlalchemy.DateTime)
