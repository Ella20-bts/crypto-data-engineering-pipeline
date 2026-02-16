CREATE TABLE IF NOT EXISTS crypto_market (
    coin_name TEXT,
    symbol TEXT,
    price NUMERIC,
    market_cap NUMERIC,
    volume NUMERIC,
    price_change_24h NUMERIC,
    extracted_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS crypto_market_current (
    coin_name TEXT,
    symbol TEXT PRIMARY KEY,
    price NUMERIC,
    market_cap NUMERIC,
    volume NUMERIC,
    price_change_24h NUMERIC,
    extracted_at TIMESTAMP
);
