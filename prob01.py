import datetime

today = datetime.date.today()
current_year = today.year

name = input('Enter your name: ')
age = int(input('Enter your age: '))

future_year = current_year + (100 - age)
print(f'{name} will turn 100 in {future_year}')
