"""
Task 1: Add movie to the collection.
Task 2: List all the movies in the collection.
Task 3: Find movie names from the collection.
"""

#menu options for user to select.
user_input = "\n Enter 'a' to add movies, 'v' view movie list, 'f' to find movies or 'q' to quit: "

#an empty list to store details of the movie
movies = []

#function for adding movies
def add_movies():
    title = input("Enter the movie name: ")
    director = input("Enter director's name: ")
    year = input("Enter release year: ")

    movies.append({
            "Title": title,
            "Director": director,
            "Year": year
    })

#function to view the movie collection
def view_movie():
    for i in movies:
        print_movies(i)

#function printing the details of the movies when required
def print_movies(i):
    print(f"Title: {i['Title']}")
    print(f"Director: {i['Director']}")
    print(f"Year: {i['Year']}")

#function to find movies details based on the title of the movie.
def find_movies():
    search_title = input("Enter the movie name you're looking for: ")

    for i in movies:
        if i['Title'] == search_title:
            print_movies(i)

#dictionary to assign functions to particular key.

user_option = {
    "a": add_movies(),
    "v": view_movie(),
    "f": find_movies()
}

#the main function of the program.
def menu():
    selection = input(user_input)
    while selection != 'q':
        if selection in user_option:
            select_function = user_option[selection]
            select_function()
        else:
            print("Wrong Selection...!!")

        selection = user_input

menu()

