from db_handler.models.crypto_raw import CryptoRaw


class DfToCryptoRawMap:
    def __init__(self) -> None:
        pass

    def create_list_from_df(self, df, process_id):
        crypto_records = []
        for index, row in df.iterrows():
            crypto_records.append(self.__row_to_crypto_raw(row, process_id))
        return crypto_records

    def __row_to_crypto_raw(self, row, process_id):

        return CryptoRaw(
            tcr_symbol_name=row["symbol"],
            tcr_status=row["status"],
            tcr_baseAsset=row["baseAsset"],
            tcr_baseAssetPrecision=row["baseAssetPrecision"],
            tcr_quoteAsset=row["quoteAsset"],
            tcr_quotePrecision=row["quotePrecision"],
            tcr_quoteAssetPrecision=row["quoteAssetPrecision"],
            tcr_baseCommissionPrecision=row["baseCommissionPrecision"],
            tcr_quoteCommissionPrecision=row["quoteCommissionPrecision"],
            tcr_icebergAllowed=row["icebergAllowed"],
            tcr_ocoAllowed=row["ocoAllowed"],
            tcr_quoteOrderQtyMarketAllowed=row["quoteOrderQtyMarketAllowed"],
            tcr_isSpotTradingAllowed=row["isSpotTradingAllowed"],
            tcr_isMarginTradingAllowed=row["isMarginTradingAllowed"],
            tcr_requestDate=row["requestDate"],
            tcr_price=row["price"],
            tcr_bidPrice_x=row["bidPrice_x"],
            tcr_bidQty_x=row["bidQty_x"],
            tcr_askPrice_x=row["askPrice_x"],
            tcr_askQty_x=row["askQty_x"],
            tcr_priceChange=row["priceChange"],
            tcr_priceChangePercent=row["priceChangePercent"],
            tcr_weightedAvgPrice=row["weightedAvgPrice"],
            tcr_prevClosePrice=row["prevClosePrice"],
            tcr_lastPrice=row["lastPrice"],
            tcr_lastQty=row["lastQty"],
            tcr_bidPrice_y=row["bidPrice_y"],
            tcr_bidQty_y=row["bidQty_y"],
            tcr_askPrice_y=row["askPrice_y"],
            tcr_askQty_y=row["askQty_y"],
            tcr_openPrice=row["openPrice"],
            tcr_highPrice=row["highPrice"],
            tcr_lowPrice=row["lowPrice"],
            tcr_volume=row["volume"],
            tcr_quoteVolume=row["volume"],
            tcr_openTime=row["openTime"],
            tcr_closeTime=row["closeTime"],
            tcr_firstId=row["firstId"],
            tcr_lastId=row["lastId"],
            tcr_count=row["count"],
            tcr_procces_id=process_id,
        )
