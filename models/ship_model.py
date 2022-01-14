from random import randint, choice

from test_bd.tests.test_data import TABLES


class Ship:

    def __init__(self, id_ship):
        self.ship = f"Ship-{id_ship+1}"
        self.weapon = f"Weapon-{randint(1, TABLES['weapons']['count'])}"
        self.hull = f"Hull-{randint(1, TABLES['hulls']['count'])}"
        self.engine = f"Engine-{randint(1, TABLES['hulls']['count'])}"

    def return_params(self):
        return self.ship, self.weapon, self.hull, self.engine

    @staticmethod
    def random_param():
        change_el = choice([('weapon', TABLES['weapons']['count'], 'Weapon-'),
                            ('hull', TABLES['hulls']['count'], 'Hull-'),
                            ('engine', TABLES['engines']['count'], 'Engine-')])
        new_value = f"{change_el[2]}{randint(1, change_el[1])}"
        return change_el[0], new_value
