from test_bd.models import Ship, Weapon, Hull, Engine
from test_bd.tests import TABLES


def generate_test_data():
    # Создаем рандомные данные
    obj_ships = [Ship(num) for num in range(TABLES['ships']['count'])]
    ships = [ship.return_params() for ship in obj_ships]

    obj_weapons = [Weapon(num) for num in range(TABLES['weapons']['count'])]
    weapons = [weapon.return_params() for weapon in obj_weapons]

    obj_hulls = [Hull(num) for num in range(TABLES['hulls']['count'])]
    hulls = [hull.return_params() for hull in obj_hulls]

    obj_engines = [Engine(num) for num in range(TABLES['engines']['count'])]
    engines = [engine.return_params() for engine in obj_engines]

    return ships, weapons, hulls, engines
