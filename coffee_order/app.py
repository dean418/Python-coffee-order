from dotenv import load_dotenv
from flask import Flask

from .blueprints.index.views import index

load_dotenv()
app = Flask(__name__)
app.register_blueprint(index, url_prefix='/')



# postgres = Database()
# postgres.drop()
# postgres.delete()