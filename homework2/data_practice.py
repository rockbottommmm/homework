from datetime import datetime, date, timedelta

def today():
    today = datetime.now().strftime('%d.%m.%Y')
    return today

def yesterday():
    delta = timedelta(days = 1)
    yesterday = (datetime.now() - delta).strftime('%d.%m.%Y')
    return yesterday
def ago_30():
    delta30 = timedelta(days = 30)
    ago_30 = (datetime.now() - delta30).strftime('%d.%m.%Y')
    return ago_30

print(f'Сегодня {today()}, вчера {yesterday()}, 30 дней назад {ago_30()}')

def making_date(date_string):
    date_needed = datetime.strptime(date_string,'%d/%m/%y %H:%M:%S.%f')
    return date_needed

date_string = "01/01/25 12:10:03.234567"
print(f'Преобразованная в дату строчка: {making_date(date_string)}')

