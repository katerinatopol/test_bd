from test_bd.models import DataBase
from test_bd.tests import NAME_DB
from test_bd.utils.generate_test_data import generate_test_data


def main():
    # Создаем базу данных
    test_db = DataBase(NAME_DB)
    test_db.create_tables()
    # Заполняем таблицы рандомными данными
    ships, weapons, hulls, engines = generate_test_data()
    test_db.insert_test_data('Ships', ships)
    test_db.insert_test_data('Weapons', weapons)
    test_db.insert_test_data('Hulls', hulls)
    test_db.insert_test_data('Engines', engines)
    # Закрываем подключение
    test_db.close_connection()


if __name__ == '__main__':
    main()
