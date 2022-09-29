user_input = "\n Enter 'a' to add movies, 'v' view movie list, 'f' to find movies or 'q' to quit: "
movies = []

def add_movies():
    title = input("Enter the movie name: ")
    director = input("Enter director's name: ")
    year = input("Enter release year: ")

    movies.append({
            "Title": title,
            "Director": director,
            "Year": year
    })

def view_movie():
    for i in movies:
        print_movies(i)

def print_movies(i):
    print(f"Title: {i['Title']}")
    print(f"Director: {i['Director']}")
    print(f"Year: {i['Year']}")

def find_movies():
    search_title = input("Enter the movie name you're looking for: ")

    for i in movies:
        if i['Title'] == search_title:
            print_movies(i)
        
user_option = {
    "a": add_movies(),
    "v": view_movie(),
    "f": find_movies()
}

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

