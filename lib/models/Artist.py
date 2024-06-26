from models.__init__ import CURSOR, CONN
from models.Concert import Concert

class Artist:

    all = {}

    def __init__(self, name, age, id = None):
        self.id = id
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Name: {self.name}' + \
               f'Age: {self.age}'
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else: 
            raise TypeError('Name must be a string...')
        
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        if isinstance(age, int):
            self._age = age
        else:
            raise TypeError('Age must be an integer...')
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS artists (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER)
        """

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS artists    
        """

        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO artists (name, age) VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.age))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, age):
        
        artist = cls(name, age)
        artist.save()
        return artist

    def update(self):
        sql = """
            UPDATE artists
            SET name = ?, age = ?
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.name, self.age, self.id))
        CONN.commit()
    
    def delete(self):
        sql = """
            DELETE FROM artists WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        artist = cls.all.get(row[0])

        if artist: 
            artist.name = row[1]
            artist.age = row[2]
        else:
            artist = cls(row[1], row[2])
            artist.id = row[0]
            cls.all[artist.id] = artist
        
        return artist
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM artists
        """

        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM artists
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT * FROM artists WHERE name = ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def concerts(self):
        sql = """
            SELECT * FROM concerts WHERE artist_id = ?
        """

        CURSOR.execute(sql, (self.id,))
        rows = CURSOR.fetchall()

        return [Concert.instance_from_db(row) for row in rows]
    
    def delete_artist_concerts(self):
        print("HERE?")
        sql = """
            SELECT * FROM concerts WHERE artist_id = ?
        """
        CURSOR.execute(sql, (self.id,))
        rows = CURSOR.fetchall()

        concerts = [Concert.instance_from_db(row) for row in rows]

        for concert in concerts:
            concert.delete()