from dotenv import load_dotenv
from flask import Flask, render_template

from .blueprints.index.views import index

load_dotenv()
app = Flask(__name__)
app.register_blueprint(index, url_prefix='/')

@app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html')

@app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html')