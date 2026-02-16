import pandas as pd
from datetime import datetime

def transform_data(raw_data):
    df = pd.DataFrame(raw_data)

    df_clean = df[[
        "name",
        "symbol",
        "current_price",
        "market_cap",
        "total_volume",
        "price_change_percentage_24h"
    ]].copy()

    df_clean.columns = [
        "coin_name",
        "symbol",
        "price",
        "market_cap",
        "volume",
        "price_change_24h"
    ]

    df_clean["extracted_at"] = datetime.now()

    print("✅ Data transformed successfully")

    return df_clean
