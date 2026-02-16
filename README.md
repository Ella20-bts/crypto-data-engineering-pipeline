🚀 Crypto Market Data Engineering Pipeline
📌 Overview

This project implements a production-style data engineering pipeline that:

Extracts cryptocurrency market data from CoinGecko API

Stores raw JSON data

Transforms data using pandas

Loads into PostgreSQL (Dockerized)

Maintains:

Historical table

Current snapshot table (UPSERT logic)

Automates daily execution using cron

Includes a Streamlit dashboard

🏗 Architecture
CoinGecko API
        ↓
Raw JSON Storage
        ↓
AWS S3 (optional)
        ↓
Transform (pandas)
        ↓
PostgreSQL (Docker)
        ↓
Historical Table
        ↓
Current Snapshot Table (UPSERT)
        ↓
Streamlit Dashboard

🛠 Tech Stack

Python

Docker

PostgreSQL

Pandas

psycopg2

boto3

Streamlit

Cron

AWS EC2

🔥 Features

Automated daily ingestion

Rate-limit handling

Production logging

Environment variable configuration

UPSERT logic for current market state

Historical time-series tracking