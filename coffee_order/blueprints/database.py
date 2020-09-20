import os
import psycopg2
from sqlalchemy import create_engine, select
from sqlalchemy import Table, Column, String, ARRAY, MetaData

class Database:
    def __init__(self):
        self.engine = create_engine(os.environ.get('PSQL_URL'))
        self.metadata = MetaData(self.engine)
        self.con = self.engine.connect()
        self.table = self.create_schema()
        self.create_table()

    def create_schema(self):
        pass

    def create_table(self):
        if not self.engine.dialect.has_table(self.engine, self.table):
            self.table.create()
        return

    def insert(self, data):
        insert_statement = self.table.insert(None).values(**data)#name=name, coffee_name=coffee_name, options=options
        self.con.execute(insert_statement)
        return

    def get_all(self):
        select_statement = self.table.select()
        documents = self.con.execute(select_statement)

        for doc in documents:
            print(doc)
        return

    def get_customer_order(self, name):
        select_statement = select([self.table]).where(self.table.columns.customer_name == name)
        return self.con.execute(select_statement).fetchall()

    def delete(self):
        delete_statement = self.table.delete(None)
        self.con.execute(delete_statement)
        return

    def drop(self):
        self.table.drop()
        return