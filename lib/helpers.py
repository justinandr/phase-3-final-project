# lib/helpers.py

from models.Artist import Artist
from models.Concert import Concert
import datetime 

def exit_program():
    print("Goodbye!")
    exit()

def get_all_artists():
    return Artist.get_all()

def find_artist_by_id(id):
    return Artist.find_by_id(id)

def display_artists(artists):
    print('\n*********************************')
    for i, artist in enumerate(artists, start=1):
        print(f'{i}. {artist.name} Age: {artist.age}')
    print('*********************************\n')

def display_concerts(artist):
    concerts = artist.concerts()
    print(f"\n{artist.name}'s Concerts")
    print('*********************************')

    for i, concert in enumerate(concerts, start=1):
        month = int(concert.date[0:2])
        day = int(concert.date[2:4])
        year = int(concert.date[4:])
        
        print(f'{i}.\nTour: {concert.tour}\n' + \
            f'Date: {datetime.date(year, month, day)}\n' + \
            f'City: {concert.city}\n' + \
            f'Venue: {concert.venue}\n') 
    print('*********************************\n')

def display_individual_concert(concert):
    month = int(concert.date[0:2])
    day = int(concert.date[2:4])
    year = int(concert.date[4:])

    print('*********************************')
    print(f'\nTour: {concert.tour}\n' + \
              f'Date: {datetime.date(year, month, day)}\n' + \
              f'City: {concert.city}\n' + \
              f'Venue: {concert.venue}\n') 
    print('*********************************\n')

def add_artist(name, age):
    Artist.create(name, age)

def update_artist(artist, name, age):
    artist.name = name
    artist.age = age
    artist.update()

def delete_artist(artist):
    artist.delete_artist_concerts()
    artist.delete()

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
    concert.delete()

def get_valid_date(date = "", new = False):
    if new == True:
        while True:
            new_date = input("Enter date: ")
            try:
                if new_date.isdigit() and len(new_date) == 8:
                    month = int(new_date[0:2])
                    day = int(new_date[2:4])
                    year = int(new_date[4:])

                    if  1 <= month <= 12 and 1 <= day <= 31 and datetime.MINYEAR <= year <= datetime.MAXYEAR:
                        return new_date
                    else:
                        print("Date must be in MMDDYYYY format and be a valid date")
                else:
                    print("Date must be in MMDDYYYY format and be a valid date")

            except Exception as exc:
                print("There was an error setting the date: ", exc)
    else:
        while True:
            new_date = input("Enter date or hit <enter> to leave as is: ")

            if new_date == "":
                return date
            try:
                if new_date.isdigit() and len(new_date) == 8:
                    month = int(new_date[0:2])
                    day = int(new_date[2:4])
                    year = int(new_date[4:])

                    if  1 <= month <= 12 and 1 <= day <= 31 and datetime.MINYEAR <= year <= datetime.MAXYEAR:
                        return new_date
                    else:
                        print("Date must be in MMDDYYYY format and be a valid date")
                else:
                    print("Date must be in MMDDYYYY format and be a valid date")

            except Exception as exc:
                print("There was an error setting the date: ", exc)
        

def get_name(name = "", new = False):
    if new == True:
        while True:
            new_name = input("Enter name: ")
            
            if new_name == "":
                print("Name cannot be left blank ")

            else: 
                return new_name
    else:
        while True:
            new_name = input("Enter new name or hit <enter> to leave as is: ")

            if new_name == "":
                return name
            else:
                return new_name


def get_age(age = "", new = False):
    if new == True:
        while True:
            new_age = input("Enter age: ")

            if new_age == "":
                print("Age cannot be left blank ")
            
            if new_age.isdigit():
                return int(new_age)
            else:
                print("Age must be a number")
    else:
        while True:
            new_age = input("Enter new age or hit <enter> to leave as is: ")

            if new_age == "":
                return age
            
            if new_age.isdigit():
                return int(new_age)
            else:
                print("Age must be a number")
    
def get_tour():
    while True:
        tour = input("Enter tour: ")

        if len(tour):
            return tour
        else:
            print("Tour cannot be left blank")
    
def get_city():
    while True:
        city = input("Enter city: ")
            
        if len(city):
            return city
        else:
            print("City cannot be left blank ")

def get_venue():
    while True:
        venue = input("Enter venue: ")
            
        if len(venue):
            return venue
        else:
            print("Venue cannot be left blank ")