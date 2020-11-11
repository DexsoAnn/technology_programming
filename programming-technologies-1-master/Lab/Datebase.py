from sqlalchemy import create_engine, Table, Column, String, Float, MetaData
from sqlalchemy.sql import select


class DB:
    def __init__(self):
        self.table = Table()
        self.engine = create_engine('sqlite:///course.sqlite3')
        self.metadate = MetaData()
        self.course = Table(
            'course',
            self.metadate,
            Column('Date', String),
            Column('ID', String),
            Column('NumCode', String),
            Column('CharCode', String),
            Column('Name', String),
            Column('Value', Float),
            Column('Previous', Float),
            Column('Diff', Float),
            Column('Price', String)
        )

    def create(self):
        self.metadate.create_all(self.engine)

    def connection(self):
        self.con = self.engine.connect()

    def write_data(self, provider):
        self.con.execute(self.course.insert(), provider)

    def print_data(self):
        for row in self.con.execute(select([self.course])):
            print(row)
