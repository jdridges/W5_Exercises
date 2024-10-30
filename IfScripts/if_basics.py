
x = 100
y = 20

#Q3 *1
if x/y == 5:
    print(f'x divided by y is 5')
    x = 1
else:
    print("Are the variables set up correctly?")

#Q3 *2
if x * y == y:
    print("Now x times y is y")
    x = 10
else:
    print(f'Whoops, x equals {x}...')

#Q3 *3
if x < y:
    print("x is less than y")
    x *= 2
else:
    print('uh oh, x is not less than y')

#Q4 *4
if x > y:
    print("how is x greater than y??")
else:
    print("x is NOT greater than y")

#Q5 *5
print(f'The final value of x is {x} and the final value of y is {y}')