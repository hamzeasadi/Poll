import psycopg2 as pg
import numpy as np


DB_name = 'myDatabase'
DB_user = 'postgres'
DB_password = 'hamze95123'
DB_port = '5432'
DB_host = 'localhost'

try:
    conn = pg.connect(database=DB_name, user=DB_user, host=DB_host,
                      password=DB_password, port=DB_port)
    print("Database Connected")

except Exception:
    print("sth went wrong")

cur = conn.cursor()
# cur.execute("""
# CREATE TABLE Employee(
# ID INT PRIMARY KEY NOT NULL,
# NAME TEXT NOT NULL,
# EMAIL TEXT NOT NULL
# )
# """)
# conn.commit()

# cur.execute("INSERT INTO Employee (ID, NAME, EMAIL) VALUES(2, 'John', 'John@gmail.com')")

cur.execute('SELECT ID, NAME, EMAIL FROM Employee')
rows = cur.fetchall()
for data in rows:
    print(f'name={data[1]} ID={data[0]} Eemail={data[2]}')

# conn.commit()
conn.close()

