import sqlite3

# Создаем базу данных и объект курсор
conn = sqlite3.connect('test_bd.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS Ships(
   userid INT PRIMARY KEY,
   fname TEXT,
   lname TEXT,
   gender TEXT);
""")
conn.commit()