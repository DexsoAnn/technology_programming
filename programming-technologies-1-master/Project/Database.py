from sqlalchemy import create_engine, Table, Column, String, Float, MetaData
from sqlalchemy.sql import select


class DB:
    def __init__(self, path_db='sqlite:///weather.sqlite3'):
        self.engine = create_engine(path_db)
        self.metadate = MetaData()
        self.weather = Table(
            'weather',
            self.metadate,
            Column('date', String),
            Column('mint', Float),
            Column('maxt', Float),
            Column('location', String),
            Column('humidity', Float),
        )

    def create(self):
        self.metadate.create_all(self.engine)

    def connection(self):
        self.con = self.engine.connect()

    def write_data(self, provider):
        self.con.execute(self.weather.insert(), provider)

    def print_data(self):
        for row in self.con.execute(select([self.weather])):
            print(row)
