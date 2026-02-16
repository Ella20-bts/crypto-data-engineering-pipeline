from extract import extract_crypto_data
from transform import transform_data
from load import load_data
from logger import setup_logger

def run_pipeline():
    logger = setup_logger()
    logger.info("🚀 Starting ETL pipeline")

    raw_data = extract_crypto_data()
    cleaned_data = transform_data(raw_data)
    load_data(cleaned_data)

    logger.info("✅ ETL pipeline completed successfully")

if __name__ == "__main__":
    run_pipeline()
