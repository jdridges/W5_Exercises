#types of iterables
str_i = 'string'
list = [1,2,3,4]
tuple = ('allspice', 'bay', 'cinnamon', 'dandelion')
range_5 = range(1,7)    #7 is stop value
dict1 = {1: 'allspice', 2:'bay', 3: 'cinnamon', 4: 'dandelion'}
counter = 0
spices = []

balance = 100
print (f'Starting balance is {balance}')

while balance > 50:
    print('Treat yourself')
    balance -= 25
    print(balance)
    if balance == 75:
        break

print(f'Your final balance is {balance}')
