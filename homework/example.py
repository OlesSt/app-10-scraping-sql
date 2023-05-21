import sqlite3

# create connection to database
connection = sqlite3.connect("data.db")
cursor = connection.cursor()

# extract all data
cursor.execute("SELECT * FROM events WHERE band = 'Lions'")
rows = cursor.fetchall()
print(rows)

# extract certain data
cursor.execute("SELECT band,date FROM events WHERE band = 'Lions'")
rows = cursor.fetchall()
print(rows)

# insert new data
new_rows = [('Cats', 'Cats City', '2088.10.17'),
            ('Hens', 'Hen City', '2088.10.17')]

cursor.executemany("INSERT INTO events VALUES(?,?,?)", new_rows)
connection.commit()

cursor.execute("SELECT * FROM events")
rows = cursor.fetchall()
print(rows)