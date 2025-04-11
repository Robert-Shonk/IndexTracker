from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from index_tracker.db import get_db
import index_tracker.query as query

bp = Blueprint('index', __name__)

@bp.route('/', methods=['GET'])
def index():
    sectors = query.get_sectors()
    
    return render_template('index/index.html', sectors=sectors)


@bp.route('/<selected_sector>', methods=['GET'])
def sector(selected_sector):
    sectors = query.get_sectors()
    stocks = query.get_stocks_by_sector(selected_sector)

    return render_template('index/stocks.html', sectors=sectors, stocks=stocks, selected_sector=selected_sector)