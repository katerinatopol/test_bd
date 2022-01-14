import sqlite3

from random import randint

from test_bd.tests.test_data import NAME_DB, TABLES  # , SHIPS_COUNT, WEAPONS_COUNT, HULLS_COUNT, ENGINES_COUNT
from test_bd.utils.generate_test_data import generate_test_data


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

    def insert_test_data(self, name_table, data):
        # Заполняем таблицы созданными данными

        self.cursor.execute(f"DELETE FROM {name_table}")
        self.cursor.executemany(f"INSERT INTO {name_table} VALUES({', '.join(['?' for _ in range(len(data[0]))])});",
                                data)
        self.connection.commit()

        # self.cursor.execute("DELETE FROM ships")
        # self.cursor.executemany("INSERT INTO ships VALUES(?, ?, ?, ?);", ships)
        # self.connection.commit()
        #
        # self.cursor.execute("DELETE FROM weapons")
        # self.cursor.executemany("INSERT INTO weapons VALUES(?, ?, ?, ?, ?, ?);", weapons)
        # self.connection.commit()
        #
        # self.cursor.execute("DELETE FROM hulls")
        # self.connection.commit()
        # self.cursor.executemany("INSERT INTO hulls VALUES(?, ?, ?, ?);", hulls)
        # self.connection.commit()
        #
        # self.cursor.execute("DELETE FROM engines")
        # self.cursor.executemany("INSERT INTO engines VALUES(?, ?, ?);", engines)
       # self.connection.commit()

    def close_connection(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()

    @staticmethod
    def select(name_db, name_table, key=None, condition=None, column='*'):
        # Открываем соединение с базой данных
        connection = sqlite3.connect(f'../{name_db}.db')
        cursor = connection.cursor()
        # Выполняем поиск
        if key and condition:
            value = cursor.execute(f"""SELECT {column} FROM {name_table} WHERE {key} = '{condition}';""").fetchall()[0]
        else:
            value = cursor.execute(f"""SELECT {column} FROM {name_table};""").fetchall()
        return value

    @staticmethod
    def check_func(data_true, data_change, name_table):
        # Дополнительная проверка, если у одного корабля не совпадают несколько значений параметров компонента.
        # По условиям в измененной базе всегда будет не совпадать только одно значение.
        name_field = list(TABLES[name_table]['columns'])
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
    ships, weapons, hulls, engines = generate_test_data()
    print(weapons)
    test_db.insert_test_data('Ships', ships)
    test_db.insert_test_data('Weapons', weapons)
    test_db.insert_test_data('Hulls', hulls)
    test_db.insert_test_data('Engines', engines)
    # test_db.insert_test_data()
    test_db.close_connection()


if __name__ == '__main__':
    main()
