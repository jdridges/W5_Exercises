favorite_movies = ['Hereditary', 'Pulp Fiction', 'Star Wars', 'Stand By Me', 'Cars']
number_of_movies = len (favorite_movies)
print("The list " + str(favorite_movies) + " includes the " + str(number_of_movies) + " movies I'd like to watch" )


#sorted 
print(sorted(favorite_movies))
print(favorite_movies)

#sorted gives it in alphabetical order vs the original list is written as it is listed


# .sort
favorite_movies.sort()
print(favorite_movies)
# when you use .sort, the list name variable saves the list in its sorted state.

#adding list items
favorite_movies.append('Benchwarmers')
print(f'{favorite_movies} is the list of movies I want to watch with Benchwarmers being the newest addition')