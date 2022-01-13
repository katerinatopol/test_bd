NAME_DB = 'wargaming'
NAME_COPY_DB = 'copy_bd'
# SHIPS_COUNT = 200
# WEAPONS_COUNT = 20
# HULLS_COUNT = 5
# ENGINES_COUNT = 6
PARAMS = {
    'weapons': ['weapon', 'reload_speed', 'rotation_speed', 'diameter', 'power_volley', 'count'],
    'hulls': ['hull', 'armor', 'type', 'capacity'],
    'engines': ['engine', 'power', 'type'],
}
TABLES = {
    'ships':
        {'name_table': 'Ships',
         'columns': {'ship': 'TEXT PRIMARY KEY',
                     'weapon': 'TEXT',
                     'hull': 'TEXT',
                     'engine': 'TEXT'},
         'foreign_key': {'weapon': 'Weapons(weapon)',
                         'hull': 'Hulls(hull)',
                         'engine': 'Engines(engine)'},
         'count': 200
         },

    'weapons':
        {'name_table': 'Weapons',
         'columns': {'weapon': 'TEXT PRIMARY KEY',
                     'reload_speed': 'INT',
                     'rotation_speed': 'INT',
                     'diameter': 'INT',
                     'power_volley': 'INT',
                     'count': 'INT'},
         'count': 20
         },

    'hulls':
        {'name_table': 'Hulls',
         'columns': {'hull': 'TEXT PRIMARY KEY',
                     'armor': 'INT',
                     'type': 'INT',
                     'capacity': 'INT'},
         'count': 5
         },

    'engines':
        {'name_table': 'Engines',
         'columns': {'engine': 'TEXT PRIMARY KEY',
                     'power': 'INT',
                     'type': 'INT'},
         'count': 6
         }
}
