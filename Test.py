import sys
import calendar
import time
import datetime


arrival = datetime.date(2016,8,1)
departure = datetime.date(2017,1,20)
test = departure - arrival
print('%s - %s = %s' %(arrival, departure, test))

Fanny = {'Arrival': datetime.date(2016,8,1), 'Departure': datetime.date(2017,1,20), 'Rent': 440}

duration = (Fanny['Departure'] - Fanny['Arrival']) / 30
incomes = duration * Fanny['Rent']

print('Duration')
print(duration)
print('Incomes')
print(incomes)
