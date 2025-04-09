from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from index_tracker.db import get_db

bp = Blueprint('index', __name__)

@bp.route('/')
def index():
    return render_template('index/index.html')