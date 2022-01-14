import os

import pytest

from . import NAME_DB, NAME_COPY_DB, TABLES
from ..models import DataBase
from ..utils.key_by_val import key_by_val


@pytest.fixture(scope='session')
def change_db():
    # создаем копию базы данных
    true_bd = DataBase(f'../{NAME_DB}')
    temporary_bd = true_bd.copy_database(NAME_COPY_DB)

    # Для каждого корабля меняем на случайный один из компонентов,
    # для каждого компонента меняем случайно выбранный параметр
    for table in TABLES.values():
        model = DataBase.models[table['name_table']]
        primary_key = key_by_val(table['columns'], 'PRIMARY KEY')
        primary_keys = [el[0] for el in temporary_bd.select(name_table=table['name_table'],
                                                            column=primary_key,
                                                            all_info=True)]
        for key in primary_keys:
            name_elem, new_value = model.random_param()
            temporary_bd.update(name_table=table['name_table'],
                                change_elem=name_elem,
                                new_val=new_value,
                                key=primary_key,
                                condition=key)

    yield temporary_bd

    # закрываем соединение и удаляем копию БД
    true_bd.close_connection()
    temporary_bd.close_connection()
    os.remove(f'{NAME_COPY_DB}.db')
