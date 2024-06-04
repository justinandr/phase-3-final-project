from models.__init__ import CURSOR, CONN
import datetime

class Concert:

    all = {}

    def __init__(self, tour, date, city, venue, artist_id, id = None):
        self.id = id
        self.tour = tour
        self.date = date
        self.city = city
        self.venue = venue
        self.artist_id = artist_id

    def __repr__(self):
        return f'Tour: {self.tour}' + \
            f'Date: {self.date}' + \
            f'City: {self.city}' + \
            f'Venue: {self.venue}' + \
            f'Artist ID: {self.artist_id}'


    @classmethod
    def instance_from_db(cls):
        pass