import sqlite3

conn = sqlite3.connect("ledger.db", check_same_thread=False)
cursor = conn.cursor()

with open("database/schema.sql") as f:
    cursor.executescript(f.read())

conn.commit()