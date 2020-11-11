import requests


class WeatherProvider:
    def __init__(self, location='Volgograd,Russia', start_date='2020-09-20', end_date='2020-09-29'):
        self.key = 'I3D60I88UB6KPSDAVGK38HNP5'
        self.url = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/weatherdata/history'
        self.location = location
        self.start_date = start_date
        self.end_date = end_date

    def convert_json_data(self):
        params = {
            'aggregateHours': 24,
            'startDateTime': f'{self.start_date}T00:0:00',
            'endDateTime': f'{self.end_date}T23:59:59',
            'unitGroup': 'metric',
            'location': self.location,
            'key': self.key,
            'contentType': 'json',
        }
        return requests.get(self.url, params).json()

    def get_list_data(self, data):
        return [
            {
                'date': row['datetimeStr'][:10],
                'mint': row['mint'],
                'maxt': row['maxt'],
                'location': 'Volgograd,Russia',
                'humidity': row['humidity'],
            }
            for row in data['locations'][self.location]['values']
        ]
