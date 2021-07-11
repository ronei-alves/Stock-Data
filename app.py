from flask import Flask, render_template, request, redirect, url_for
from models import Stock
import yfinance as yf
import locale

app = Flask(__name__)
app.secret_key = 'badkey'
app.config.from_pyfile('app_cfg.py')

# ===================================

stocks = []


def add_stock(ticker, country):
    stock = Stock(ticker, country)
    stocks.append(stock)


add_stock('ITSA4.SA', 'BR')
add_stock('VOO', 'EUA')
add_stock('WEGE3.SA', 'BR')
add_stock('KO', 'EUA')


# ===================================


# Views
@app.route('/')
def index():
    return render_template('index.html', stocks=stocks)


@app.route('/new_stock')
def new_stock():
    return render_template('new_stock.html')


@app.route('/save_stock', methods=['POST', ])
def save_stock():
    # =================================================================================
    stock = Stock(request.form['ticker'].upper(),
                  request.form['country'])
    stocks.append(stock)
    # =================================================================================
    return redirect(url_for('index'))


@app.route('/edit_stock/<int:stock_id>')
def edit_stock(stock_id):
    return render_template('edit.html', stock_id=stock_id,
                           stock=stocks[stock_id - 1])


@app.route('/update_stock', methods=['POST', ])
def update_stock():
    # =================================================================================
    stock = stocks[int(request.form['stock_id']) - 1]
    stock.ticker = request.form['ticker'].upper()
    stock.country = request.form['country']
    # =================================================================================
    return redirect(url_for('index'))


@app.route('/remove_stock/<int:stock_id>')
def remove_stock(stock_id):
    # =================================================================================
    stock_index = stock_id - 1
    del (stocks[stock_index])
    # =================================================================================
    return redirect(url_for('index'))


@app.route('/get_price/<int:stock_id>')
def get_price(stock_id):
    stock = stocks[stock_id - 1]
    price = str(yf.Ticker(stock.ticker).info['regularMarketPrice'])

    if stock.country == 'EUA':
        locale.setlocale(locale.LC_MONETARY, 'en_US.UTF-8')
        price = str(locale.currency(float(price)))
    else:
        locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
        price = str(locale.currency(float(price)))

    stock.price = price
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
