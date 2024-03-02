#WAP to ask the user to enter names of their favourite movies and store them in a list

#without using append method
movie1 = input("Enter name of your favourite movie 1 : ")
movie2 = input("Enter name of your favourite movie 2 : ")
movie3 = input("Enter name of your favourite movie 3 : ")

movies = [movie1,movie2,movie3]

print(movies)

#with using append method

movies = []

movie1 = input("Enter name of your favourite movie 1 : ")
movie2 = input("Enter name of your favourite movie 2 : ")
movie3 = input("Enter name of your favourite movie 3 : ")

movies.append(movie1)
movies.append(movie2)
movies.append(movie3)

print(movies)