from sqlalchemy import create_engine
from sqlalchemy import Table, Column, String, Integer, ARRAY, MetaData

from .database import Database

class Order(Database):
    def __init__(self):
        Database.__init__(self)

    def create_schema(self):
        return Table('orders', self.metadata,
        Column('customer_name', String),
        Column('drink_name', String),
        Column('options', ARRAY(String), nullable=True))