import os
from random import choice, randint
import sqlite3

import pytest

from .test_data import NAME_DB, WEAPONS_COUNT, HULLS_COUNT, ENGINES_COUNT


@pytest.fixture(scope='session')
def change_db():
    # TODO убрать повторения, реорганизовать
    # создаем копию базы данных
    connection = sqlite3.connect(f'../{NAME_DB}.db')
    cursor = connection.cursor()
    cursor.execute("""vacuum into './copy_bd.db';""")
    connection.close()
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

    yield time_base, tb_cursor

    # закрываем соединение и удаляем копию БД
    time_base.close()
    os.remove('./copy_bd.db')


def data_true():
    # Открываем соединение с базой данных
    connection = sqlite3.connect(f'../{NAME_DB}.db')
    cursor = connection.cursor()
    data_weapons = []
    data_hulls = {}
    data_engines = {}
    print('test-3')
    # Формируем список PRIMARY KEYS
    ships = [el[0] for el in cursor.execute("""SELECT ship FROM Ships""").fetchall()]
    # Для каждого PRIMARY KEY
    for ship in ships:
        true_el = cursor.execute("""SELECT weapon, hull, engine FROM Ships WHERE ship = ?;""",
                                     (ship, )).fetchall()[0]
        data_weapons.append((ship, true_el[0]))
        # data_weapons[f'{ship}'] = true_el[0]
        # data_hulls[f'{ship}'] = true_el[1]
        # data_engines[f'{ship}'] = true_el[2]
    print('test-4')
    return {'weapons': data_weapons, 'hulls': data_hulls, 'engines': data_engines}


def data_change():
    # Открываем соединение с базой данных
    time_base = sqlite3.connect('./copy_bd.db')
    tb_cursor = time_base.cursor()
    data_weapons = []
    data_hulls = {}
    data_engines = {}
    print('test-3')
    # Формируем список PRIMARY KEYS
    ships = [el[0] for el in tb_cursor.execute("""SELECT ship FROM Ships""").fetchall()]
    # Для каждого PRIMARY KEY
    for ship in ships:
        change_el = tb_cursor.execute("""SELECT weapon, hull, engine FROM Ships WHERE ship = ?;""",
                                          (ship, )).fetchall()[0]
        print(change_el)
        data_weapons.append((ship, change_el[0]))
        # data_weapons[f'{ship}'] = change_el[0]
        # data_hulls[f'{ship}'] = change_el[1]
        # data_engines[f'{ship}'] = change_el[2]
    print('test-4')
    print(data_weapons)
    return {'weapons': data_weapons, 'hulls': data_hulls, 'engines': data_engines}


