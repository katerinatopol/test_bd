from random import choice, randint
import sqlite3

import pytest

from test_data import NAME_DB, WEAPONS_COUNT, HULLS_COUNT, ENGINES_COUNT


# @pytest.fixture
def change_db(scope='session'):
    # TODO убрать повторения, реорганизовать
    # создаем копию базы данных
    connection = sqlite3.connect(f'../{NAME_DB}.db')
    cursor = connection.cursor()
    cursor.execute("""vacuum into './copy_bd.db';""")
    time_base = sqlite3.connect('./copy_bd.db')
    tb_cursor = time_base.cursor()

    # Для каждого корабля меняем на случайный один из компонентов
    ships = [el[0] for el in tb_cursor.execute("""SELECT ship FROM Ships""").fetchall()]
    for ship in ships:
        change_el = choice([('weapon', WEAPONS_COUNT, 'Weapon-'),
                            ('hull', HULLS_COUNT, 'Hull-'),
                            ('engine', ENGINES_COUNT, 'Engine-')])
        new_value = f"{change_el[2]}{randint(1, change_el[1])}"
        tb_cursor.execute(f"UPDATE Ships SET {change_el[0]} = '{new_value}' WHERE ship = ?;", (ship,))
    time_base.commit()

    # Для каждого компонента меняем случайно выбранный параметр
    weapons = [el[0] for el in tb_cursor.execute("""SELECT weapon FROM Weapons""").fetchall()]
    for weapon in weapons:
        change_el = choice(['reload_speed', 'rotation_speed', 'diameter', 'power_volley', 'count'])
        new_value = randint(1, 20)
        tb_cursor.execute(f"UPDATE Weapons SET {change_el} = '{new_value}' WHERE weapon = ?;", (weapon,))
    time_base.commit()

    hulls = [el[0] for el in tb_cursor.execute("""SELECT hull FROM Hulls""").fetchall()]
    for hull in hulls:
        change_el = choice(['armor', 'type', 'capacity'])
        new_value = randint(1, 20)
        tb_cursor.execute(f"UPDATE Hulls SET {change_el} = '{new_value}' WHERE hull = ?;", (hull,))
    time_base.commit()

    engines = [el[0] for el in tb_cursor.execute("""SELECT engine FROM Engines""").fetchall()]
    for engine in engines:
        change_el = choice(['power', 'type'])
        new_value = randint(1, 20)
        tb_cursor.execute(f"UPDATE Engines SET {change_el} = '{new_value}' WHERE engine = ?;", (engine,))
    time_base.commit()

    return time_base

change_db()
