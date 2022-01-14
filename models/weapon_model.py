from random import randint, choice

from test_bd.tests.test_data import VALUE_RANGE, TABLES


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

    @staticmethod
    def random_param():
        change_el = choice(list(TABLES['weapons']['columns'].keys())[1:])
        new_value = randint(1, VALUE_RANGE)
        return change_el, new_value
