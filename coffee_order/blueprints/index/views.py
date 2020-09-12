from flask import Blueprint, render_template, redirect, url_for, request

from .database import Database

postgres = Database()

index = Blueprint('index', __name__, template_folder='templates')

@index.route('/')
def get_index():
    return render_template('index.html')

@index.route('/add-to-order', methods=['POST'])
def add_to_order():
    for item in request.form:
        if not request.form[item]:
            return render_template('index.html', err='please fill in form')

    options = []

    if 'decaf' in request.form:
        options.append('decaf')

    if 'extra_shot' in request.form:
        options.append('extra_shot')

    postgres.insert(request.form['name'], request.form['coffee'], options)

    print('--------')
    postgres.get_all()
    print('--------')

    return redirect('/')