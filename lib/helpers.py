# lib/helpers.py

from models.Artist import Artist
from models.Concert import Concert


def exit_program():
    print("Goodbye!")
    exit()

def get_all_artists():
    return Artist.get_all()

def find_artist_by_id(id):
    return Artist.find_by_id(id)

def get_concerts(artist):
    print(artist)
    return artist.concerts()

def display_artists(artists):
    print('\n*********************************')
    for i, artist in enumerate(artists, start=1):
        print(f'{i}. {artist.name} Age: {artist.age}')
    print('*********************************\n')

def display_concerts(concerts):
    print(concerts[0])
    print(f"\n{Artist.find_by_id(concerts[0].artist_id).name}'s Concerts")
    print('*********************************')
    for i, concert in enumerate(concerts, start=1):
        print(f'{i}.\nTour: {concert.tour}\n' + \
              f'Date: {concert.date}\n' + \
              f'City: {concert.city}\n' + \
              f'Venue: {concert.venue}\n') 
    print('*********************************\n')

def display_individual_concert(concert):
    print('*********************************')
    print(f'\nTour: {concert.tour}\n' + \
              f'Date: {concert.date}\n' + \
              f'City: {concert.city}\n' + \
              f'Venue: {concert.venue}\n') 
    print('*********************************\n')

def add_artist(name, age):
    Artist.create(name, age)

def update_artist(artist, name, age):
    if name == "" and age == "":
        pass
    elif name == "":
        artist.age = int(age)
    elif age == "":
        artist.name = name
    else:
        artist.name = name
        artist.age = int(age)

    Artist.update(artist)

def delete_artist(artist):
    Artist.delete_artist_concerts(artist)
    Artist.delete(artist)

def update_concert(concert, tour, date, city, venue):
    if tour == "":
        tour = concert.tour
    if date == "":
        date = concert.date
    if city == "":
        city = concert.city
    if venue == "":
        venue = concert.venue

    concert.tour = tour
    concert.date = date
    concert.city = city
    concert.venue = venue

    Concert.update(concert)

def add_concert(tour, date, city, venue, artist_id):
    Concert.create(tour, date, city, venue, artist_id)

def delete_concert(concert):
    Concert.delete(concert)

def get_valid_date(date = "", new = False):
    if new == True:
        while True:
            new_date = input("Enter date: ")
            try:
                if isinstance(new_date, str) and len(new_date) == 8:
                    return new_date
                else:
                    print("Date must be in MMDDYYYY format")

            except Exception as exc:
                print("There was an error setting the date: ", exc)
    
    while True:
        new_date = input("Enter date or hit <enter> to leave as is: ")

        if new_date == "":
            return date
        try:
            if isinstance(new_date, str) and len(new_date) == 8:
                return new_date
            else:
                print("Date must be in MMDDYYYY format")

        except Exception as exc:
            print("There was an error setting the date: ", exc)
        

def get_name():
    while True:
        name = input("Enter name: ")
        
        if name == "":
            print("Name cannot be left blank ")

        else: 
            return name
    
def get_age():
    while True:
        age = input("Enter age: ")

        if age == "":
            print("Age cannot be left blank ")

        return int(age)
    
def get_tour():
    while True:
        tour = input("Enter tour: ")

        if tour == "":
            print("Tour cannot be left blank ")

        return tour
    
def get_city():
    while True:
        city = input("Enter city: ")
            
        if city == "":
            print("City cannot be left blank ")

        return city

def get_venue():
    while True:
        venue = input("Enter venue: ")
            
        if venue == "":
            print("Venue cannot be left blank ")

        return venue