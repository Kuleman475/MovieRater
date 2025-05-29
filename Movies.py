import sqlite3

con = sqlite3.connect("Movies.db")
cur = con.cursor()
for row in cur.execute('SELECT * FROM movies ORDER BY stars'):
    print(row)