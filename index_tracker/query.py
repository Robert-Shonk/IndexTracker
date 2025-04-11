from index_tracker.db import get_db

# write queries here and return where needed.
def get_sectors():
    db = get_db()
    sectors = db.execute(
        """
            SELECT snp.sector, SUM(stock.market_cap) as total_market_cap,
            (SUM(stock.current_price)/SUM(stock.previous_price)-1)*100 as move
            FROM stock
            JOIN snp ON stock.symbol = snp.symbol
            GROUP BY sector
            ORDER BY total_market_cap DESC;
        """
    ).fetchall()

    return sectors


def get_stocks():
    db = get_db()

    stocks = db.execute(
        """
            SELECT stock.*, ((stock.current_price/stock.previous_price)-1)*100 as move,
            snp.security, snp.sector, snp.sub_industry
            FROM stock
            JOIN snp ON stock.symbol = snp.symbol
            ORDER BY stock.market_cap DESC;
        """
    ).fetchall()

    return stocks


def get_stocks_by_sector(sector):
    db = get_db()
    stocks = db.execute(
        """
            SELECT stock.*, snp.security, snp.sector, snp.sub_industry, ((stock.current_price/stock.previous_price)-1)*100 as move
            FROM stock
            JOIN snp ON stock.symbol = snp.symbol
            WHERE snp.sector = ?
            ORDER BY stock.market_cap DESC;
        """,
        (sector,)
    ).fetchall()

    return stocks

def get_max_mc_by_sector(sector):
    db = get_db()
    max_market_cap = db.execute(
        """
            SELECT MAX(stock.market_cap) FROM stock
            JOIN snp ON stock.symbol = snp.symbol
            WHERE sector = ?;
        """,
        (sector,)
    ).fetchone()

    return max_market_cap