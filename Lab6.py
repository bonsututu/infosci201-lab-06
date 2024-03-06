class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def equip(self, weapon):
        self.weapon = weapon

class Hero(Character):
    def __init__(self, name, health):
        super().__init__(name, health)

class Enemy(Character):
    def __init__(self, name, health, weapon):
        super().__init__(name, health)
        self.weapon = weapon

class Weapon:
    def __init__(self, name, weapon_type, damage, value):
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = value

empty_handed = Weapon(name="Empty handed",
               weapon_type="dummy",
               damage=0,
               value=0)
healing_staff = Weapon(name="Healing Staff",
               weapon_type="magic",
               damage=-3,
               value=0)


protagonist = Hero(name="Hero", health=100)
protagonist.health = 10
protagonist.equip(empty_handed)
ally = Enemy(name="Friendly Enemy", health=100, weapon=healing_staff)