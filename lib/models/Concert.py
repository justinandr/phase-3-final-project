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
    
    @property
    def tour(self):
        return self.tour
    
    @tour.setter
    def tour(self, tour):
        if isinstance(tour, str) and len(tour):
            self.tour = tour
        else:
            raise ValueError('Tour must be a non-empty string...')
        
    @property
    def date(self):
        return self.date
    
    @date.setter
    def date(self, date):
        if isinstance(date, str) and len(date) == 8:
            month = int(date[0:2])
            day = int(date[2:4])
            year = int(date[4:])

            self.date = datetime.date(year, month, day)
            #This is not done

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS concerts (
            id INTEGER PRIMARY KEY,
            tour TEXT,
            date TEXT,
            city TEXT,
            venue TEXT,
            FOREIGN KEY (artist_id) REFERENCES artists(id)
            )
        """

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS concerts
        """

        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO concerts (tour, date, city, venue, artist_id)
            VALUES (?, ?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.tour, self.date, self.city, self.venue, self.artist_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def instance_from_db(cls):
        pass