DROP TABLE IF EXISTS snp;
DROP TABLE IF EXISTS stock;

CREATE TABLE snp (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    symbol TEXT UNIQUE NOT NULL,
    security TEXT NOT NULL,
    sector TEXT NOT NULL,
    sub_industry TEXT NOT NULL,
    hq_location TEXT NOT NULL,
    date_added TEXT NOT NULL, -- date added to S&P500 list
    CIK TEXT NOT NULL,
    founded INTEGER NOT NULL,
    date_recorded TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE stock (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    symbol TEXT UNIQUE NOT NULL,
    market_cap REAL NOT NULL,
    current_price REAL NOT NULL,
    previous_price REAL NOT NULL,
    PE_ratio REAL NOT NULL,
    day_low REAL NOT NULL,
    day_high REAL NOT NULL,
    year_week_low REAL NOT NULL,
    year_week_high REAL NOT NULL,
    date_recorded TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);