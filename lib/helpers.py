# lib/helpers.py

from models.Artist import Artist
from models.Concert import Concert

def exit_program():
    print("Goodbye!")
    exit()

def get_all_artists():
    return Artist.get_all()

def get_concerts(artist):
    return Artist.concerts(artist)

def display_artists(artists):
    print('\n*********************************')
    for i, artist in enumerate(artists, start=1):
        print(f'{i}. {artist.name}')
    print('*********************************\n')

def display_concerts(concerts):
    print('\n*********************************')
    print(Artist.find_by_id(concert.artist_id).name)
    for i, concert in enumerate(concerts, start=1):
        print(f'{i}. Tour: {concert.tour}\n' + \
              f'Date: {concert.date}' + \
              f'City: {concert.city}' + \
              f'Venue: {concert.venue}') 
    print('*********************************\n')

def add_artist():
    pass

def edit_artist():
    pass

def add_concert():
    pass

def edit_concert():
    pass