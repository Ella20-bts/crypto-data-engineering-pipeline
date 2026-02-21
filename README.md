# Crypto Market Intelligence Platform

Automated Data Engineering Pipeline with PostgreSQL, Docker, and Real-Time Analytics

---

## Overview

This project is a fully containerized data engineering platform that ingests live cryptocurrency market data, stores it in PostgreSQL, and exposes analytics through an interactive dashboard.

The system demonstrates production-style architecture including:

- Scheduled ETL pipeline
- Historical and current snapshot tables
- UPSERT logic
- Containerized infrastructure
- Modular Python package structure
- Interactive analytics layer
- Docker Compose orchestration

---

## Architecture

External Crypto API  
        ↓  
ETL Scheduler (Python)  
        ↓  
PostgreSQL (Data Warehouse)  
        ↓  
Streamlit Intelligence Dashboard  
        ↓  
Docker Network  

---

## Tech Stack

- Python 3.11
- PostgreSQL 15
- Docker & Docker Compose
- Streamlit
- Plotly
- Pandas
- psycopg2
- GitHub Actions (CI Ready)

---

## Data Model

### 1. crypto_market (Historical Table)

Stores time-series historical data for each coin.

Columns:
- coin_name
- symbol
- price
- market_cap
- volume
- price_change_24h
- extracted_at

### 2. crypto_market_current (Snapshot Table)

Maintains the latest state of each asset using UPSERT logic.

---

## Key Features

### Automated ETL Scheduler
Runs continuously inside Docker using a scheduler loop.

### Historical Tracking
Every ETL run appends to the historical table.

### UPSERT Logic
Ensures snapshot table always reflects latest state.

### Advanced Analytics Dashboard
Includes:
- Executive summary metrics
- Market dominance
- Volatility analysis
- Liquidity metrics
- Top gainers/losers
- Historical price trends

---

## Business Metrics Implemented

- Market Dominance (%)
- Volatility (Std Dev of 24h change)
- Liquidity Score (Volume / Market Cap)
- Top 3 Concentration Ratio
- Historical Price Trend Analysis

---

## How To Run Locally

### 1. Clone Repository
git clone https://github.com/your-username/crypto-data-engineering-pipeline.git</br>
cd crypto-data-engineering-pipeline

### 2. Build & Start Services
docker-compose build
docker-compose up -d

### 3. Run ETL Once (Optional)
docker-compose run etl

### 4. Open Dashboard
http://localhost:8501


---

## Container Services

- crypto-postgres
- crypto-etl (Scheduled pipeline)
- crypto-dashboard

---

## Production Design Considerations

- Modular package structure (src/)
- Proper import resolution
- Environment-based configuration
- Database initialization scripts
- Persistent volume storage
- Clean separation of services

---

## Future Enhancements

- AWS EC2 deployment
- RDS migration
- CI/CD auto-deployment
- Nginx reverse proxy
- HTTPS configuration
- Docker Hub publishing
- Infrastructure as Code

---

## Author

Louella Respuesto  
Data Engineering & Analytics
