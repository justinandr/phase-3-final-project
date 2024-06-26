#!/usr/bin/env python3

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

def main_menu():
    print("Please make a selection: ")
    print("Type a to view Artists")
    print("Type e to exit the program")

def artist_menu():
    artists = get_all_artists()

    if artists:
        display_artists(artists)

        print("Type the number of the artist to see their concerts")
        print("Type a to add an artist")
        print("Type d to delete an artist")
        print("Type u to update an artist")
        print("Type b to go back")
        print("Type e to exit the program")
        
        while True:
            choice = input("> ")
            if choice.lower() == "a":
                name = get_name("", True)
                age = get_age("", True)
                add_artist(name, age)
                artist_menu()
            elif choice.lower() == "b":
                main()
            elif choice.lower() == "u":
                to_update = input("Enter the artist number you would like to update: ")
                name = get_name(artists[int(to_update) -1].name, False)
                age = get_age(artists[int(to_update) - 1].age)
                update_artist(artists[int(to_update) - 1], name, age)
                artist_menu()
            elif choice.lower() == "d":
                to_delete = input("Enter the artist number you would like to delete: ")
                delete_artist(artists[int(to_delete) - 1])
                artist_menu()
            elif choice.lower() == "e":
                exit_program()
            elif choice.isdigit() and int(choice) > 0 and int(choice) <= len(artists):
                concert_menu(artists[int(choice) - 1])
            else:
                print("Invalid choice")

    else:
        print('\n*********************************')
        print("There are no artists to display")
        print('*********************************\n')
        print("Type a to add an artist")
        print("Type b to go back")
        print("Type e to exit the program")

        while True:
            choice = input("> ")
            if choice.lower() == "a":
                name = get_name()
                age = get_age("", True)
                add_artist(name, age)
                artist_menu()
            elif choice.lower() == "b":
                main()
            elif choice.lower() == "e":
                exit_program()
            else:
                print("Invalid choice")

def concert_menu(artist):
    if artist.concerts():
        display_concerts(artist)
    else:
        print('\n*********************************')
        print("This artist has no saved concerts")
        print('*********************************\n')
        print("Type a to add a concert")
        print("Type b to go back")
        print("Type e to exit the program")

        while True:
            choice = input("> ")
            if choice.lower() == "a":
                tour = get_tour()
                date = get_valid_date("", True)
                city = get_city()
                venue = get_venue()
                add_concert(tour, date, city, venue, artist.id)
                concert_menu(artist)
            elif choice.lower() == "b":
                artist_menu()
            elif choice.lower() == "e":
                exit_program()
            else:
                print("Invalid choice")


    print("Type the number of the concert to view it")
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
            tour = get_tour()
            date = get_valid_date("", True)
            city = get_city()
            venue = get_venue()
            add_concert(tour, date, city, venue, artist.id)
            concert_menu(artist)
        elif choice == "":
            print("Invalid choice")
        elif choice.isdigit() and int(choice) > 0 and int(choice) <= len(artist.concerts()):
            concerts = artist.concerts()
            individual_concert_menu(concerts[int(choice) - 1])
        else:
            print("Invalid choice")

def individual_concert_menu(concert):
    display_individual_concert(concert)

    print("Type u to update this concert")
    print("Type d to delete this concert")
    print("Type b to go back")
    print("Type e to exit the program")

    while True:
        choice = input("> ")
        if choice.lower() == "u":
            tour = input("Enter tour name or hit <enter> to leave as is: ")
            date = get_valid_date(concert.date)
            city = input("Enter city or hit <enter> to leave as is: ")
            venue = input("Enter venue or hit <enter> to leave is: ")
            update_concert(concert, tour, date, city, venue)
            individual_concert_menu(concert)
        elif choice.lower() == "d":
            id = concert.artist_id
            delete_concert(concert)
            concert_menu(find_artist_by_id(id))
        elif choice.lower() == "b":
            concert_menu(find_artist_by_id(concert.artist_id))
        elif choice.lower() == "e":
            exit_program()
        else:
            print("Invalid choice")




if __name__ == "__main__":
    main()