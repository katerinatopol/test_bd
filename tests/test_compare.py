import pytest

from test_bd.create_bd import DataBase
from test_bd.tests.conftest import change_db
from test_bd.tests.test_data import NAME_COPY_DB, NAME_DB, TABLES


class Test:

    @staticmethod
    @pytest.mark.parametrize('ship, true_weapon', DataBase.select(name_db=NAME_DB, name_table='Ships',
                                                                  column='ship, weapon'))
    def test_for_weapon(change_db, ship, true_weapon):
        change_weapon = DataBase.select(name_db=NAME_COPY_DB, name_table='Ships', key='ship',
                                        condition=ship, column='weapon')[0]
        assert true_weapon == change_weapon, f'{ship}, {change_weapon}: expected {true_weapon}, was {change_weapon}'

        data_true = DataBase.select(name_db=NAME_DB, name_table='Weapons', key='weapon', condition=true_weapon)
        data_change = DataBase.select(name_db=NAME_COPY_DB, name_table='Weapons', key='weapon',
                                      condition=change_weapon)
        check, message = DataBase.check_func(data_true, data_change, 'weapons')
        assert check, f'{ship}, {true_weapon}: {message}'

    @staticmethod
    @pytest.mark.parametrize('ship, true_hull', DataBase.select(name_db=NAME_DB, name_table='Ships',
                                                                column='ship, hull'))
    def test_for_hull(change_db, ship, true_hull):
        change_hull = DataBase.select(name_db=NAME_COPY_DB, name_table='Ships', key='ship',
                                      condition=ship, column='hull')[0]
        assert true_hull == change_hull, f'{ship}, {change_hull}: expected {true_hull}, was {change_hull}'

        data_true = DataBase.select(name_db=NAME_DB, name_table='Hulls', key='hull', condition=true_hull)
        data_change = DataBase.select(name_db=NAME_COPY_DB, name_table='Hulls', key='hull', condition=change_hull)
        check, message = DataBase.check_func(data_true, data_change, 'hulls')
        assert check, f'{ship}, {true_hull}: {message}'

    @staticmethod
    @pytest.mark.parametrize('ship, true_engine', DataBase.select(name_db=NAME_DB, name_table='Ships',
                                                                  column='ship, engine'))
    def test_for_engine(change_db, ship, true_engine):
        change_engine = DataBase.select(name_db=NAME_COPY_DB, name_table='Ships', key='ship',
                                        condition=ship, column='engine')[0]
        assert true_engine == change_engine, f'{ship}, {change_engine}: expected {true_engine}, was {change_engine}'

        data_true = DataBase.select(name_db=NAME_DB, name_table='Engines', key='engine', condition=true_engine)
        data_change = DataBase.select(name_db=NAME_COPY_DB, name_table='Engines',
                                      key='engine', condition=change_engine)
        check, message = DataBase.check_func(data_true, data_change, 'engines')
        assert check, f'{ship}, {true_engine}: {message}'
