#aws settings
AWS_SECRET_NAME = "prod/binance/api"
AWS_REGION_NAME = "us-east-1"


#File management constants
CSV_FOLDER = "data/csv/"
JSON_FOLDER = "data/json/"
PARQUET_FOLDER = "data/parquet/"
CSV_EXTENSION = ".csv"
PARQUET_EXTENSION = ".parquet.gzip"
UTF8_ENCODING = "utf-8"
GZIP_COMPRESSION="gzip"
LOG_FOLDER = "logs/"
LOG_NAME = "binance_real_time"
LOG_EXTENSION = ".log"

#format constants
DATE_FOR_FILES = "_%Y%m%d_%H%M%S"
LOG_FORMAT = "%(asctime)s %(message)s"

#binance endpoints
BINANCE_API_BASE_URL = "https://api.binance.com/api/v3/"
BINANCE_API_EXCHANGE_INFO = "exchangeInfo"
BINANCE_API_KLINES = "klines"
BINANCE_API_PRICES = "ticker/price"

#///api/v3/ticker/price
