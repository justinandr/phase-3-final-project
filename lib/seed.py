#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.Artist import Artist
from models.Concert import Concert

def main():
    Artist.drop_table()
    Concert.drop_table()
    Artist.create_table()
    Concert.create_table()

    Artist.create('Celine Dion', 56)
    Artist.create('Michael Buble', 48)

    Concert.create("Let's Talk About Love", "08211998", "Boston", "FleetCenter", 1)
    Concert.create("Let's Talk About Love", "09031998", "New York City", "Madison Square Garden", 1)
    Concert.create("Let's Talk About Love", "12071998", "Montreal", "Molson Center", 1)
    Concert.create("Let's Talk About Love", "01311999", "Tokyo", "Tokyo Dome", 1)
    Concert.create("Let's Talk About Love", "06191999", "Paris", "Stade de France", 1)
    Concert.create("Crazy Love", "03202010", "New York City", "Madison Square Garden", 2)
    Concert.create("Crazy Love", "04032010", "Seattle", "KeyArena", 2)
    Concert.create("Crazy Love", "05232010", "Milan", "Mediolanum Forum", 2)
    Concert.create("Crazy Love", "04182012", "Stockholm", "Ericsson Globe", 2)

if __name__ == "__main__":
    main()