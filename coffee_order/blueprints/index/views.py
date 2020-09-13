from flask import Blueprint, render_template, redirect, url_for, request

from .orders import Order
order = Order()

index = Blueprint('index', __name__, template_folder='templates')

@index.route('/')
def get_index():
    return render_template('index.html')


@index.route('/customer/<name>')
def show_orders(name):
    orders = order.get_customer_order('dean')
    return render_template('index.html', orders=orders)


@index.route('/add-to-order', methods=['POST'])
def add_to_order():
    for item in request.form:
        if not request.form[item]:
            return render_template('index.html', err='please fill in form')

    new_order = {
        'customer_name': request.form['name'],
        'drink_name': request.form['coffee'],
        'options': []
    }

    if 'decaf' in request.form:
        new_order['options'].append('decaf')

    if 'extra_shot' in request.form:
        new_order['options'].append('extra_shot')

    order.insert(new_order)
    order.get_all()

    return redirect(f'/customer/{request.form["name"]}')