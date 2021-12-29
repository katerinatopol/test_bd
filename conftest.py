from random import choice, randint
import sqlite3

import pytest


# @pytest.fixture
def change_db(scope='session'):
    # создаем копию базы данных
    connection = sqlite3.connect('test_bd.db')
    cursor = connection.cursor()
    cursor.execute("""vacuum into 'copy_bd.db';""")
    time_base = sqlite3.connect('copy_bd.db')
    tb_cursor = time_base.cursor()

    ships = [el[0] for el in tb_cursor.execute("""SELECT ship FROM Ships""").fetchall()]
    for ship in ships:
        change_el = choice(['weapon', 'hull', 'engine'])
        new_value = 1000000000000000000
        cmd = f'UPDATE Ships SET {change_el} = {new_value} WHERE ship = {ship};'
        tb_cursor.execute(cmd)


change_db()
