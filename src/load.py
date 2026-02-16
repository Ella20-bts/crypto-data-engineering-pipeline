import os
import psycopg2

def load_data(df):
    try:
        # Read environment variables
        DB_HOST = os.getenv("DB_HOST", "localhost")
        DB_NAME = os.getenv("DB_NAME", "crypto_db")
        DB_USER = os.getenv("DB_USER", "admin")
        DB_PASSWORD = os.getenv("DB_PASSWORD", "admin123")
        DB_PORT = os.getenv("DB_PORT", "5432")

        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )

        cursor = conn.cursor()

        for _, row in df.iterrows():
            # Historical table
            cursor.execute("""
                INSERT INTO crypto_market (
                    coin_name,
                    symbol,
                    price,
                    market_cap,
                    volume,
                    price_change_24h,
                    extracted_at
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (
                row["coin_name"],
                row["symbol"],
                row["price"],
                row["market_cap"],
                row["volume"],
                row["price_change_24h"],
                row["extracted_at"]
            ))

            # Current snapshot table (UPSERT)
            cursor.execute("""
                INSERT INTO crypto_market_current (
                    coin_name,
                    symbol,
                    price,
                    market_cap,
                    volume,
                    price_change_24h,
                    extracted_at
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (symbol)
                DO UPDATE SET
                    price = EXCLUDED.price,
                    market_cap = EXCLUDED.market_cap,
                    volume = EXCLUDED.volume,
                    price_change_24h = EXCLUDED.price_change_24h,
                    extracted_at = EXCLUDED.extracted_at;
            """, (
                row["coin_name"],
                row["symbol"],
                row["price"],
                row["market_cap"],
                row["volume"],
                row["price_change_24h"],
                row["extracted_at"]
            ))

        conn.commit()
        cursor.close()
        conn.close()

        print("✅ Data inserted (history) and upserted (current) successfully!")

    except Exception as e:
        print("❌ Error loading data:")
        print(e)
