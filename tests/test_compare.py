import pytest

from test_bd.create_bd import DataBase
from test_bd.tests.conftest import change_db
from test_bd.tests.test_data import NAME_COPY_DB, NAME_DB, PARAMS


class Test:

    @staticmethod
    @pytest.mark.parametrize('ship, true_weapon', DataBase.select_all_ships(NAME_DB)['weapons'])
    def test_for_weapon(change_db, ship, true_weapon):
        change_weapon = DataBase.select_one(NAME_COPY_DB, 'Ships', 'ship', ship, 'weapon')[0]
        assert true_weapon == change_weapon, f'{ship}, {change_weapon}: expected {true_weapon}, was {change_weapon}'

        data_true = DataBase.select_one(NAME_DB, 'Weapons', 'weapon', true_weapon)
        data_change = DataBase.select_one(NAME_COPY_DB, 'Weapons', 'weapon', change_weapon)
        check, message = DataBase.check_func(data_true, data_change, PARAMS['weapons'])
        assert check, f'{ship}, {true_weapon}: {message}'

    @staticmethod
    @pytest.mark.parametrize('ship, true_hull', DataBase.select_all_ships(NAME_DB)['hulls'])
    def test_for_hull(change_db, ship, true_hull):
        change_hull = DataBase.select_one(NAME_COPY_DB, 'Ships', 'ship', ship, 'hull')[0]
        assert true_hull == change_hull, f'{ship}, {change_hull}: expected {true_hull}, was {change_hull}'

        data_true = DataBase.select_one(NAME_DB, 'Hulls', 'hull', true_hull)
        data_change = DataBase.select_one(NAME_COPY_DB, 'Hulls', 'hull', change_hull)
        check, message = DataBase.check_func(data_true, data_change, PARAMS['hulls'])
        assert check, f'{ship}, {true_hull}: {message}'

    @staticmethod
    @pytest.mark.parametrize('ship, true_engine', DataBase.select_all_ships(NAME_DB)['engines'])
    def test_for_engine(change_db, ship, true_engine):
        change_engine = DataBase.select_one(NAME_COPY_DB, 'Ships', 'ship', ship, 'engine')[0]
        assert true_engine == change_engine, f'{ship}, {change_engine}: expected {true_engine}, was {change_engine}'

        data_true = DataBase.select_one(NAME_DB, 'Engines', 'engine', true_engine)
        data_change = DataBase.select_one(NAME_COPY_DB, 'Engines', 'engine', change_engine)
        check, message = DataBase.check_func(data_true, data_change, PARAMS['engines'])
        assert check, f'{ship}, {true_engine}: {message}'

