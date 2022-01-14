from random import randint, choice

from test_bd.tests.test_data import VALUE_RANGE, TABLES


class Engine:

    def __init__(self, id_engine):
        self.engine = f'Engine-{id_engine + 1}'
        self.power = randint(1, VALUE_RANGE)
        self.type = randint(1, VALUE_RANGE)

    def return_params(self):
        return self.engine, self.power, self.type

    @staticmethod
    def random_param():
        change_el = choice(list(TABLES['engines']['columns'].keys())[1:])
        new_value = randint(1, VALUE_RANGE)
        return change_el, new_value
