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
    return Artist.concerts(artist)

def display_artists(artists):
    print('\n*********************************')
    for i, artist in enumerate(artists, start=1):
        print(f'{i}. {artist.name} Age: {artist.age}')
    print('*********************************\n')

def display_concerts(concerts):
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

def update_artist():
    pass

def add_concert():
    pass

def edit_concert():
    pass