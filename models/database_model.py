import sqlite3

from test_bd.models import Ship, Weapon, Hull, Engine
from test_bd.tests.test_data import TABLES


class DataBase:

    models = {'Ships': Ship, 'Weapons': Weapon, 'Hulls': Hull, 'Engines': Engine}

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
        self.cursor.execute(f"DELETE FROM {name_table}")
        self.cursor.executemany(f"INSERT INTO {name_table} VALUES({', '.join(['?' for _ in range(len(data[0]))])});",
                                data)
        self.connection.commit()

    def close_connection(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()

    def update(self, name_table, change_elem, new_val, key, condition):
        self.cursor.execute(f"UPDATE {name_table} SET {change_elem} = '{new_val}' WHERE {key} = ? ;", (condition, ))
        self.connection.commit()

    def select(self, name_table, key=None, condition=None, column='*', all_info=False):
        if key and condition:
            value = self.cursor.execute(f"""SELECT {column} FROM {name_table} WHERE {key} = '{condition}';""").fetchall()
        else:
            value = self.cursor.execute(f"""SELECT {column} FROM {name_table};""").fetchall()

        if all_info:
            return value
        else:
            return value[0]

    def copy_database(self, name_new_db):
        self.cursor.execute(f"""vacuum into '{name_new_db}.db';""")

        return DataBase(name_new_db)

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
