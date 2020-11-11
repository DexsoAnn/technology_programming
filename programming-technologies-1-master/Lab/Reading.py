import requests


class Provider:
    def __init__(self):
        self.date = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()

    def get_list_data(self):
        return [
            {
                'Date': self.date['Date'],
                'ID': self.date['Valute'][i]['ID'],
                'NumCode': self.date['Valute'][i]['NumCode'],
                'CharCode': self.date['Valute'][i]['CharCode'],
                'Name': self.date['Valute'][i]['Name'],
                'Value': float(self.date['Valute'][i]['Value']),
                'Previous': float(self.date['Valute'][i]['Previous']),
                'Diff': float(self.date['Valute'][i]['Previous']) - float(self.date['Valute'][i]['Value']),
                'Price': 'Up' if (float(self.date['Valute'][i]['Previous']) - float(self.date['Valute'][i]['Value'])) > 0 else 'Down'
            }
            for i in self.date['Valute']
        ]
