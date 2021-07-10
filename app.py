from flask import Flask, render_template, request, redirect, url_for
from models import Stock

app = Flask(__name__)
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

print(stocks)

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
    add_stock(request.form['ticker'].upper(),
              request.form['country'])
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
