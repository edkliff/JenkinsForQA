from app import app
from flask import redirect, render_template


@app.route('/')
@app.route('/main')
def index():
    return render_template('base.html')
