from index_tracker.db import get_db

# write queries here and return where needed.
def get_sectors():
    db = get_db()
    sectors = db.execute('SELECT sector FROM snp GROUP BY sector').fetchall()

    return sectors


def get_stocks():
    db = get_db()

    stocks = db.execute(
        """
            SELECT stock.*, ((stock.current_price/stock.previous_price)-1)*100 as move,
            snp.security, snp.sector, snp.sub_industry
            FROM stock
            JOIN snp ON stock.symbol = snp.symbol;
        """
    ).fetchall()

    return stocks