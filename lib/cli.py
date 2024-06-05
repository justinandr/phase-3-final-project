# lib/cli.py

from helpers import *


def main():
    while True:
        main_menu()
        choice = input("> ")
        if choice.lower() == "e":
            exit_program()
        elif choice.lower() == "a":
            artist_menu()
        else:
            print("Invalid choice")

#list options
def main_menu():
    print("Please make a selection: ")
    print("Type a to view Artists")
    print("Type e to exit the program")

#list artists and list options (add the add artist function)
def artist_menu():
    artists = get_all_artists()
    display_artists(artists)

    print("Type the number of the artist to see their details")
    print("Type b to go back")
    print("Type e to exit the program")
    
    while True:
        choice = input("> ")
        if choice.lower() == "b":
            main()
        elif choice.lower() == "e":
            exit_program()
        elif int(choice) > 0 and int(choice) <= len(artists):
            concert_menu(artists[int(choice) - 1])
        else:
            print("Invalid choice")

#display concerts based on artist selection and list options
def concert_menu(artist):
    print(type(artist))
    print(artist)
    concerts = get_concerts(artist)
    display_concerts(concerts)

    print("Type the number of a concert to edit it")
    print("Type a to add a concert")
    print("Type b to go back")
    print("Type e to exit the program")

    while True:
        choice = input("> ")
        if choice.lower() == "b":
            artist_menu()
        elif choice.lower() == "e":
            exit_program()
        elif choice.lower() == "a":
            pass
        elif int(choice) > 0 and int(choice) <= len(concerts):
            pass


if __name__ == "__main__":
    main()
