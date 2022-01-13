import pytest

from test_bd.tests.conftest import change_db, data_true, data_change


class Test:

    @staticmethod
    @pytest.mark.parametrize('ship, true_weapon', data_true()['weapons'])
    def test_for_weapon(change_db, ship, true_weapon):
        # print(data_true()['weapons'])
        # print(true_weapon)
        # ship = 1
        change_data = data_change()['weapons']
        change_weapon = [el[1] for el in change_data if el[0] == ship][0]
        assert true_weapon == change_weapon, f'{ship}, {change_weapon}: expected {true_weapon}, was {change_weapon}'
    #
    # @staticmethod
    # @pytest.mark.parametrize('ship, true_hull, change_hull', data_true()['hulls'])
    # def test_for_hull(ship, true_hull, change_hull):
    #     assert true_hull == change_hull, f'{ship}, {change_hull}: expected {true_hull}, was {change_hull}'
    #
    # @staticmethod
    # @pytest.mark.parametrize('ship, true_engine, change_engine', data_true()['engines'])
    # def test_for_engine(ship, true_engine, change_engine):
    #     assert true_engine == change_engine, f'{ship}, {change_engine}: expected {true_engine}, was {change_engine}'
    #
