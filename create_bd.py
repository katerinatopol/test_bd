import sqlite3

from random import randint

try:
    # Создаем базу данных и объект курсор
    connection = sqlite3.connect('test_bd.db')
    cursor = connection.cursor()

    # TODO связи ключей

    # Создаем таблицу Ships
    cursor.execute("""CREATE TABLE IF NOT EXISTS Ships(
       ship TEXT PRIMARY KEY,
       weapon TEXT,
       hull TEXT,
       engine TEXT);
    """)
    connection.commit()

    # Создаем таблицу Weapons
    cursor.execute("""CREATE TABLE IF NOT EXISTS Weapons(
       weapon TEXT PRIMARY KEY,
       reload_speed INT,
       rotation_speed INT,
       diameter INT,
       power_volley INT,
       count INT);
    """)
    connection.commit()

    # Создаем таблицу Hulls
    cursor.execute("""CREATE TABLE IF NOT EXISTS Hulls(
       hull TEXT PRIMARY KEY,
       armor INT,
       type INT,
       capacity INT);
    """)
    connection.commit()

    # Создаем таблицу Engines
    cursor.execute("""CREATE TABLE IF NOT EXISTS Engines(
       engine TEXT PRIMARY KEY,
       power INT,
       type INT);
    """)
    connection.commit()


    # Создаем рандомные данные
    ships = [(f'Ship-{i+1}', f'Weapon-{i+1}', f'Hull-{i+1}', f'Engine-{i+1}') for i in range(200)]
    weapons = [(f'Weapon-{i+1}', randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20))
               for i in range(20)]
    hulls = [(f'Hull-{i+1}', randint(1, 20), randint(1, 20), randint(1, 20)) for i in range(5)]
    engines = [(f'Engine-{i+1}', randint(1, 20), randint(1, 20)) for i in range(6)]


    # Заполняем таблицы созданными данными
    # TODO продумать объекты/модели

    cursor.execute("DELETE FROM ships")
    connection.commit()

    cursor.executemany("INSERT INTO ships VALUES(?, ?, ?, ?);", ships)
    connection.commit()

    cursor.execute("DELETE FROM weapons")
    connection.commit()

    cursor.executemany("INSERT INTO weapons VALUES(?, ?, ?, ?, ?, ?);", weapons)
    connection.commit()

    cursor.execute("DELETE FROM hulls")
    connection.commit()

    cursor.executemany("INSERT INTO hulls VALUES(?, ?, ?, ?);", hulls)
    connection.commit()

    cursor.execute("DELETE FROM engines")
    connection.commit()

    cursor.executemany("INSERT INTO engines VALUES(?, ?, ?);", engines)
    connection.commit()

except sqlite3.Error as error:
    print(f"Ошибка при подключении к sqlite {error}")

finally:
    if connection:
        cursor.close()
        connection.close()
