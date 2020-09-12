import os
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, String, ARRAY, MetaData

class Database:
    def __init__(self):
        self.engine = create_engine(os.environ.get('PSQL_URL'))
        self.metadata = MetaData(self.engine)
        self.con = self.engine.connect()
        self.order_table = self.create_schema()

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