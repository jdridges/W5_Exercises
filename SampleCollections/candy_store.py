candy_types = ('gummy bears', 'skittles', 'sour punch')
flavors = ('lime', 'blue rasperry', 'strawberry')

candy_combinations = set()

candy_combinations.add((candy_types[0], flavors[0]))            #gummy bears, lime
candy_combinations.add((candy_types[2], flavors[1]))     #sour punch, blue rasperry
candy_combinations.add((candy_types[0], flavors[2]))            #gummy bears, strawberry


print(f'Today\'s candy options include: {candy_combinations}')

#The 