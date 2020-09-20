from sqlalchemy import create_engine
from sqlalchemy import Table, Column, String, Integer, MetaData

from ..database import Database

class Coffee(Database):
    def __init__(self):
        Database.__init__(self)

    def create_schema(self):
        return Table('coffee', self.metadata,
        Column('name', String),
        Column('price', Integer))