import sqlite3

from random import randint

from test_bd.tests.test_data import NAME_DB, TABLES  # , SHIPS_COUNT, WEAPONS_COUNT, HULLS_COUNT, ENGINES_COUNT


class DataBase:

    def __init__(self, name):
        self.name = name
        try:
            self.connection = sqlite3.connect(f'{name}.db')
            self.cursor = self.connection.cursor()

        except sqlite3.Error as error:
            print(f"Ошибка при подключении к sqlite {error}")

    def create_tables(self):
        for table in TABLES.values():
            columns = ', '.join([f'{key} {val}' for key, val in table['columns'].items()])
            try:
                foreign_key = ', '.join(
                        [f'FOREIGN KEY ({key}) REFERENCES {val}' for key, val in table['foreign_key'].items()])
                columns += f', {foreign_key}'
            except KeyError as error:
                pass

            try:
                self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS {table['name_table']}({columns});""")
                self.connection.commit()
            except sqlite3.Error as error:
                print(f"Ошибка при подключении к sqlite {error}")
        # try:
        #     # Создаем таблицу Ships
        #     self.cursor.execute("""CREATE TABLE IF NOT EXISTS Ships(
        #        ship TEXT PRIMARY KEY,
        #        weapon TEXT,
        #        hull TEXT,
        #        engine TEXT,
        #        FOREIGN KEY (weapon) REFERENCES Weapons(weapon),
        #        FOREIGN KEY (hull) REFERENCES Hulls(hull),
        #        FOREIGN KEY (engine) REFERENCES Engines(engine));
        #     """)
        #     self.connection.commit()
        #
        #     # Создаем таблицу Weapons
        #     self.cursor.execute("""CREATE TABLE IF NOT EXISTS Weapons(
        #        weapon TEXT PRIMARY KEY,
        #        reload_speed INT,
        #        rotation_speed INT,
        #        diameter INT,
        #        power_volley INT,
        #        count INT);
        #     """)
        #     self.connection.commit()
        #
        #     # Создаем таблицу Hulls
        #     self.cursor.execute("""CREATE TABLE IF NOT EXISTS Hulls(
        #        hull TEXT PRIMARY KEY,
        #        armor INT,
        #        type INT,
        #        capacity INT);
        #     """)
        #     self.connection.commit()
        #
        #     # Создаем таблицу Engines
        #     self.cursor.execute("""CREATE TABLE IF NOT EXISTS Engines(
        #        engine TEXT PRIMARY KEY,
        #        power INT,
        #        type INT);
        #     """)
        #     self.connection.commit()
        #
        # except sqlite3.Error as error:
        #     print(f"Ошибка при подключении к sqlite {error}")

    def insert_test_data(self):

        # Создаем рандомные данные
        ships = [(f'Ship-{i + 1}', f'Weapon-{randint(1, 20)}', f'Hull-{randint(1, 5)}', f'Engine-{randint(1, 6)}')
                 for i in range(TABLES['ships']['count'])]
        weapons = [(f'Weapon-{i + 1}', randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20))
                   for i in range(TABLES['weapons']['count'])]
        hulls = [(f'Hull-{i + 1}', randint(1, 20), randint(1, 20), randint(1, 20))
                 for i in range(TABLES['hulls']['count'])]
        engines = [(f'Engine-{i + 1}', randint(1, 20), randint(1, 20)) for i in range(TABLES['engines']['count'])]

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

    @staticmethod
    def select_all_ships(name_db):
        # Открываем соединение с базой данных
        connection = sqlite3.connect(f'../{name_db}.db')
        cursor = connection.cursor()
        data_weapons = []
        data_hulls = []
        data_engines = []
        # Формируем список PRIMARY KEYS
        ships = [el[0] for el in cursor.execute("""SELECT ship FROM Ships""").fetchall()]
        # Для каждого PRIMARY KEY
        for ship in ships:
            elem = cursor.execute("""SELECT weapon, hull, engine FROM Ships WHERE ship = ?;""",
                                  (ship,)).fetchall()[0]
            data_weapons.append((ship, elem[0]))
            data_hulls.append((ship, elem[1]))
            data_engines.append((ship, elem[2]))
        return {'weapons': data_weapons, 'hulls': data_hulls, 'engines': data_engines}

    @staticmethod
    def select_one(name_db, name_table, key, condition, column='*'):
        # Открываем соединение с базой данных
        connection = sqlite3.connect(f'../{name_db}.db')
        cursor = connection.cursor()
        # Выполняем поиск
        value = cursor.execute(f"""SELECT {column} FROM {name_table} WHERE {key} = '{condition}';""").fetchall()[0]
        return value

    @staticmethod
    def check_func(data_true, data_change, name_field):
        # Дополнительная проверка, если у одного корабля не совпадают несколько значений параметров компонента.
        # По условиям в измененной базе всегда будет не совпадать только одно значение.
        message = ''
        check = True
        for ind, el in enumerate(name_field[1:], 1):
            if data_true[ind] != data_change[ind]:
                message += f'{name_field[ind]} expected {data_true[ind]}, was {data_change[ind]}; '
                check = False

        return check, message


def main():
    test_db = DataBase(NAME_DB)
    test_db.create_tables()
    test_db.insert_test_data()
    test_db.close_connection()


if __name__ == '__main__':
    main()
