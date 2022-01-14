from random import randint, choice

from test_bd.tests.test_data import VALUE_RANGE, TABLES


class Hull:

    def __init__(self, id_hull):
        self.hull = f'Hull-{id_hull + 1}'
        self.armor = randint(1, VALUE_RANGE)
        self.type = randint(1, VALUE_RANGE)
        self.capacity = randint(1, VALUE_RANGE)

    def return_params(self):
        return self.hull, self.armor, self.type, self.capacity

    @staticmethod
    def random_param():
        change_el = choice(list(TABLES['hulls']['columns'].keys())[1:])
        new_value = randint(1, VALUE_RANGE)
        return change_el, new_value
