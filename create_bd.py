import sqlite3

from random import randint

from test_data import SHIPS_COUNT, WEAPONS_COUNT, HULLS_COUNT, ENGINES_COUNT


class DataBase:

    def __init__(self, name):
        self.name = name
        try:
            self.connection = sqlite3.connect(f'{name}.db')
            self.cursor = self.connection.cursor()

        except sqlite3.Error as error:
            print(f"Ошибка при подключении к sqlite {error}")

    def create_tables(self):
        try:
            # Создаем таблицу Ships
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS Ships(
               ship TEXT PRIMARY KEY,
               weapon TEXT,
               hull TEXT,
               engine TEXT,
               FOREIGN KEY (weapon) REFERENCES Weapons(weapon),
               FOREIGN KEY (hull) REFERENCES Hulls(hull),
               FOREIGN KEY (engine) REFERENCES Engines(engine));
            """)
            self.connection.commit()

            # Создаем таблицу Weapons
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS Weapons(
               weapon TEXT PRIMARY KEY,
               reload_speed INT,
               rotation_speed INT,
               diameter INT,
               power_volley INT,
               count INT);
            """)
            self.connection.commit()

            # Создаем таблицу Hulls
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS Hulls(
               hull TEXT PRIMARY KEY,
               armor INT,
               type INT,
               capacity INT);
            """)
            self.connection.commit()

            # Создаем таблицу Engines
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS Engines(
               engine TEXT PRIMARY KEY,
               power INT,
               type INT);
            """)
            self.connection.commit()

        except sqlite3.Error as error:
            print(f"Ошибка при подключении к sqlite {error}")

    def insert_test_data(self):

        # Создаем рандомные данные
        ships = [(f'Ship-{i + 1}', f'Weapon-{randint(1, 20)}', f'Hull-{randint(1, 5)}', f'Engine-{randint(1, 6)}')
                 for i in range(SHIPS_COUNT)]
        weapons = [(f'Weapon-{i + 1}', randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20))
                   for i in range(WEAPONS_COUNT)]
        hulls = [(f'Hull-{i + 1}', randint(1, 20), randint(1, 20), randint(1, 20)) for i in range(HULLS_COUNT)]
        engines = [(f'Engine-{i + 1}', randint(1, 20), randint(1, 20)) for i in range(ENGINES_COUNT)]

        # Заполняем таблицы созданными данными

        self.cursor.execute("DELETE FROM ships")
        self.connection.commit()
        self.cursor.executemany("INSERT INTO ships VALUES(?, ?, ?, ?);", ships)
        self.connection.commit()

        self.cursor.execute("DELETE FROM weapons")
        self.connection.commit()
        self.cursor.executemany("INSERT INTO weapons VALUES(?, ?, ?, ?, ?, ?);", weapons)
        self.connection.commit()

        self.cursor.execute("DELETE FROM hulls")
        self.connection.commit()
        self.cursor.executemany("INSERT INTO hulls VALUES(?, ?, ?, ?);", hulls)
        self.connection.commit()

        self.cursor.execute("DELETE FROM engines")
        self.connection.commit()
        self.cursor.executemany("INSERT INTO engines VALUES(?, ?, ?);", engines)
        self.connection.commit()

    def close_connection(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()


def main():
    test_db = DataBase('wargaming')
    test_db.create_tables()
    test_db.insert_test_data()
    test_db.close_connection()


if __name__ == '__main__':
    main()
