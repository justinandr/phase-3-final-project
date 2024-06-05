import sqlite3

CONN = sqlite3.connect('tour_dates.db')
CURSOR = CONN.cursor()
