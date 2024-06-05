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
    print("Type a to add an artist")
    print("Type d to delete an artist")
    print("Type u to update an artist")
    print("Type b to go back")
    print("Type e to exit the program")
    
    while True:
        choice = input("> ")
        if choice.lower() == "a":
            name = input("Enter the artist's name: ")
            age = int(input("Enter the artist's age: "))
            add_artist(name, age)
            artist_menu()
        elif choice.lower() == "b":
            main()
        elif choice.lower() == "u":
            to_update = input("Enter the artist number you would like to update: ")
            name = input("Enter new name or hit <enter> to leave as is: ")
            age = input("Enter new age or hit <enter> to leave as is: ")
            update_artist(artists[int(to_update) - 1], name, age)
            artist_menu()
        elif choice.lower() == "d":
            to_delete = input("Enter the artist number you would like to delete: ")
            delete_artist(artists[int(to_delete) - 1])
            artist_menu()
        elif choice.lower() == "e":
            exit_program()
        elif int(choice) > 0 and int(choice) <= len(artists):
            concert_menu(artists[int(choice) - 1])
        else:
            print("Invalid choice")

#display concerts based on artist selection and list options
def concert_menu(artist):
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
