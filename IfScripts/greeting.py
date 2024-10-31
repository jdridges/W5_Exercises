import datetime


time_of_day = datetime.datetime.now().hour

if time_of_day < 10:
        greeting = 'Good morning'
elif 10 <= time_of_day < 17:
        greeting = 'Good day'
else:
        greeting = 'Good evening'

print(f'The hour of day is {time_of_day}')
print(greeting)