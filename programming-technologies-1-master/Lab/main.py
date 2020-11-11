import requests
from Lab.Datebase import DB
from Lab.Reading import Provider


provider = Provider()
db = DB()

db.create()

db.connection()

data = provider.get_list_data()

db.write_data(data)

db.print_data()
