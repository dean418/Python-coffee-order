
import os
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, String, ARRAY, MetaData
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect

load_dotenv()
app = Flask(__name__) # first param tells flask whats part of our app

class Database:
    def __init__(self):
        db_string = f"postgres://{os.environ.get('PSQL_USER')}:{os.environ.get('PSQL_PASSWORD')}@127.0.0.1:5432"
        self.engine = create_engine(db_string)
        self.metadata = MetaData(self.engine)
        self.con = self.engine.connect()
        self.order_table = self.create_schema()

        # self.create_table()
    def create_schema(self):
        return Table('orders', self.metadata,
        Column('name', String),
        Column('coffee_name', String),
        Column('options', ARRAY(String), nullable = True))

    def insert(self, name, coffee_name, options):
        insert_statement = self.order_table.insert(None).values(name=name, coffee_name=coffee_name, options=options)
        self.con.execute(insert_statement)
        return

    def create_table(self):
        self.order_table.create()
        return

    def get_all(self):
        select_statement = self.order_table.select()
        result_set = self.con.execute(select_statement)

        for r in result_set:
            print(r)
        return

    def delete(self):
        delete_statement = self.order_table.delete(None)
        self.con.execute(delete_statement)
        return

    def drop(self):
        self.order_table.drop()
        return

postgres = Database()
# postgres.drop()
postgres.delete()
postgres.get_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add-to-order', methods=['POST'])
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
    postgres.get_all()

    return redirect('/')