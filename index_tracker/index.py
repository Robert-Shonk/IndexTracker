from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from index_tracker.db import get_db

bp = Blueprint('index', __name__)

@bp.route('/', methods=['GET'])
def index():
    db = get_db()
    sectors = db.execute('SELECT sector FROM snp GROUP BY sector').fetchall()
    stocks = db.execute(
        """
            SELECT *, ((stock.current_price/stock.previous_price)-1)*100 as move FROM stock
            JOIN snp ON stock.symbol = snp.symbol;
        """
    ).fetchall()

    return render_template('index/index.html', stocks=stocks, sectors=sectors)