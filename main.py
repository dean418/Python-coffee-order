
import os
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, String, ARRAY, MetaData
from dotenv import load_dotenv
from flask import Flask, render_template, request

load_dotenv()
app = Flask(__name__) # first param tells flask whats part of our app

db_string = f"postgres://{os.environ.get('PSQL_USER')}:{os.environ.get('PSQL_PASSWORD')}@127.0.0.1:5432"

engine = create_engine(db_string)
metadata = MetaData(engine)

order_table = Table('orders', metadata,
    Column('name', String),
    Column('coffee_name', String),
    Column('options', ARRAY(String)))

con = engine.connect()

# Create table
    # order_table.create()

# Basic insert
    # insert_statement = order_table.insert().values(name='Dean', coffee_name='latte', options=['extra shot', 'decaf'])
    # con.execute(insert_statement)

# Get all orders
select_statement = order_table.select()
result_set = con.execute(select_statement)

for r in result_set:
    print(r)

# Basic delete
    # delete_statement = order_table.delete()
    # con.execute(delete_statement)

# -------- old connection --------
# try:
#     connection = psycopg2.connect(
#         user= os.environ.get('PSQL_USER'),
#         password=os.environ.get('PSQL_PASSWORD'),
#         host=os.environ.get('PSQL_HOST'),
#         port=os.environ.get('PSQL_PORT'),
#         database=os.environ.get('PSQL_DATABASE'))
#     print(connection)
#     cursor = connection.cursor()

# except (Exception, psycopg2.Error) as error:
#     print ('Error while connecting to PostgreSQL', error)
#     exit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add-to-order', methods=['POST'])
def add_to_order():
    name = request.form['name']
