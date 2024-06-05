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
        return self._tour
    
    @tour.setter
    def tour(self, tour):
        if isinstance(tour, str) and len(tour):
            self._tour = tour
        else:
            raise ValueError('Tour must be a non-empty string...')
        
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        if isinstance(date, str) and len(date) == 8:
            month = int(date[0:2])
            day = int(date[2:4])
            year = int(date[4:])

            self._date = datetime.date(year, month, day)
            #This is not done

        self._date = date

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS concerts (
            id INTEGER PRIMARY KEY,
            tour TEXT,
            date TEXT,
            city TEXT,
            venue TEXT,
            artist_id INTEGER,
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
    def create(cls, tour, date, city, venue, artist_id):
        concert = cls(tour, date, city, venue, artist_id)
        concert.save()
        return concert

    def update(self):
        sql = """
            UPDATE concerts
            SET tour = ?, date = ?, city = ?, venue = ?, artist_id = ?
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.tour, self.date, self.city, self.venue, self.artist_id, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM artists
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        concert = cls.all.get(row[0])

        if concert:
            concert.tour = row[1]
            concert.date = row[2]
            concert.city = row[3]
            concert.venue = row[4]
            concert.artist_id = row[5]

        else:
            concert = cls(row[1], row[2], row[3], row[4], row[5])
            concert.id = row[0]
            cls.all[concert.id] = concert

        return concert
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM concerts
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM concerts WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT * FROM concerts WHERE name = ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None