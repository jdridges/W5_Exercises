import datetime


# time_of_day = datetime.datetime.now().hour
time_of_day = 3
if 23<= time_of_day < 4:
       greeting = 'What are you doing up so late???'
elif time_of_day < 10:
        greeting = 'Good morning'
elif 10 <= time_of_day < 17:
        greeting = 'Good day'
elif 17<= time_of_day<23:
    greeting = 'Good evening'

print(f'The hour of day is {time_of_day}')
print(greeting)