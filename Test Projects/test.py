import sqlite3

conn = sqlite3.connect("database")
cursor = conn.cursor()

query = "text"
embedding_query = [0.1, 0.2]
threshold = 12

cursor.execute("SELECT * FROM entries"
               "WHERE ")