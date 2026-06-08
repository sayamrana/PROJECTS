import mysql.connector

conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    port=3307
)

cursor = conn.cursor()

cursor.execute("SHOW DATABASES")

for db in cursor.fetchall():
    print(db)

conn.close()