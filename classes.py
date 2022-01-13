# TODO нет функционала

class Ship:

    def __init__(self, ship, weapon, hull, engine):
        self.ship = ship
        self.weapon = weapon
        self.hull = hull
        self.engine = engine


class Weapon:

    def __init__(self, weapon, reload_speed, rotation_speed, diameter, power_volley, count):
        self.weapon = weapon
        self.reload_speed = reload_speed
        self.rotation_speed = rotation_speed
        self.diameter = diameter
        self.power_volley = power_volley
        self.count = count


class Hull:

    def __init__(self, hull, armor, type, capacity):
        self.hull = hull
        self.armor = armor
        self.type = type
        self.capacity = capacity


class Engine:

    def __init__(self, engine, power, type):
        self.engine = engine
        self.power = power
        self.type = type


print(dir(Hull))