from flask import Flask, render_template, request, redirect, url_for, session
import psycopg2
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # used to manage session securely

# Get DB connection using environment variables (secure for production)
def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ['DB_HOST'],
        database=os.environ['DB_NAME'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD']
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM products')
    products = cur.fetchall()  # list of tuples: (id, name, price)
    cur.close()
    conn.close()
    return render_template('index.html', products=products)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    # session stores cart items in user browser (in memory)
    cart = session.get('cart', [])
    cart.append(product_id)
    session['cart'] = cart
    return redirect(url_for('index'))

@app.route('/cart')
def cart():
    cart = session.get('cart', [])
    conn = get_db_connection()
    cur = conn.cursor()
    if cart:
        cur.execute('SELECT * FROM products WHERE id = ANY(%s)', (cart,))
        items = cur.fetchall()
    else:
        items = []
    cur.close()
    conn.close()
    return render_template('cart.html', items=items)

@app.route('/checkout')
def checkout():
    session.pop('cart', None)
    return 'Checkout complete!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)