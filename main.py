
import psycopg2
import sqlalchemy
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request

load_dotenv()
app = Flask(__name__) # first param tells flask whats part of our app

try:
    connection = psycopg2.connect(
        user= os.environ.get('PSQL_USER'),
        password=os.environ.get('PSQL_PASSWORD'),
        host=os.environ.get('PSQL_HOST'),
        port=os.environ.get('PSQL_PORT'),
        database=os.environ.get('PSQL_DATABASE'))

    cursor = connection.cursor()

except (Exception, psycopg2.Error) as error:
    print ('Error while connecting to PostgreSQL', error)
    exit()

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        print(request.form['title'])

    return render_template('index.html')