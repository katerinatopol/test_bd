import sqlite3

import pytest


@pytest.fixture
def change_db(scope='session'):
    connection = sqlite3.connect('test_bd.db')
    cursor = connection.cursor()
    cursor.execute("""vacuum into 'copy_bd.db';""")


