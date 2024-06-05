# lib/cli.py

from helpers import *


def main():
    while True:
        main_menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            artist_menu()
        else:
            print("Invalid choice")

#list options
def main_menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. View Artists")

#list artists and list options (add the add artist function)
def artist_menu():
    artists = get_all_artists()
    display_artists(artists)

    print("Select the number of the artist to see their details")
    print("Type b to go back")
    print("0. Exit the program")
    
    while True:
        print("are we in there?")
        choice = input("> ")
        if choice == "B" or "b":
            main()
        elif choice == "0":
            exit_program()
        else:
            print("Invalid choice")
        
        concert_menu(artists[int(choice) - 1])

#display concerts based on artist selection and list options
def concert_menu(artist):
    print(get_concerts(artist))


if __name__ == "__main__":
    main()
