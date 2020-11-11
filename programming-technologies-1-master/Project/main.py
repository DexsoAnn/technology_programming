from Project.Database import DB
from Project.Reading import WeatherProvider
print('Введите пожалуйста ваши данные:')
print('Привер: Volgograd,Russia 2020-09-20 2020-09-29')
Data = input().split()

weather = WeatherProvider() if len(Data) == 0 else WeatherProvider(*Data)
db = DB()

db.create()

db.connection()

data = weather.convert_json_data()

db.write_data(weather.get_list_data(data))

db.print_data()


