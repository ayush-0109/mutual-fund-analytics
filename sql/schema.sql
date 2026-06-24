CREATE TABLE dim_fund (
    amfi_code INTEGER PRIMARY KEY,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT,
    risk_category TEXT
);

CREATE TABLE dim_date (
    date_id INTEGER PRIMARY KEY,
    full_date DATE,
    year INTEGER,
    month INTEGER,
    quarter INTEGER
);

CREATE TABLE fact_transactions (
    transaction_id INTEGER PRIMARY KEY,
    investor_id TEXT,
    amfi_code INTEGER,
    transaction_date DATE,
    amount_inr REAL,
    transaction_type TEXT
);

CREATE TABLE fact_nav (
    amfi_code INTEGER,
    nav_date DATE,
    nav REAL
)