from random import randint

from test_bd.tests.test_data import TABLES, VALUE_RANGE


class Ship:

    def __init__(self, id_ship):
        self.ship = f"Ship-{id_ship}"
        self.weapon = f"Weapon-{randint(1, TABLES['weapons']['count'])}"
        self.hull = f"Hull-{randint(1, TABLES['hulls']['count'])}"
        self.engine = f"Engine-{randint(1, TABLES['hulls']['count'])}"

    def return_params(self):
        return self.ship, self.weapon, self.hull, self.engine


class Weapon:

    def __init__(self, id_weapon):
        self.weapon = f'Weapon-{id_weapon + 1}'
        self.reload_speed = randint(1, VALUE_RANGE)
        self.rotation_speed = randint(1, VALUE_RANGE)
        self.diameter = randint(1, VALUE_RANGE)
        self.power_volley = randint(1, VALUE_RANGE)
        self.count = randint(1, VALUE_RANGE)

    def return_params(self):
        return self.weapon, self.reload_speed, self.rotation_speed, self.diameter, self.power_volley, self.count


class Hull:

    def __init__(self, id_hull):
        self.hull = f'Hull-{id_hull + 1}'
        self.armor = randint(1, VALUE_RANGE)
        self.type = randint(1, VALUE_RANGE)
        self.capacity = randint(1, VALUE_RANGE)

    def return_params(self):
        return self.hull, self.armor, self.type, self.capacity


class Engine:

    def __init__(self, id_engine):
        self.engine = f'Engine-{id_engine + 1}'
        self.power = randint(1, VALUE_RANGE)
        self.type = randint(1, VALUE_RANGE)

    def return_params(self):
        return self.engine, self.power, self.type
