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

    