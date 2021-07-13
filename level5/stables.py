"""Horse stuff here."""


class SameFoodException(Exception):

    def __init__(self, message: str):
        super(message)


class HorseFood:

    def __init__(self, name: str, food_type: str, hunger_points: int):
        self.name = name
        self.food_type = food_type
        self.hunger_points = hunger_points


class Horse:

    def __init__(self, color: str, age: int, gender: str):
        self.color = color
        self.age = age
        self.gender = gender
        self.stamina = 100
        self.cleanness = 100
        self.tummy_full = 100
        self.food_eaten = []

    def feed_horse(self, food: HorseFood):
        if len(self.food_eaten) >= 3 and self.all_match(self.food_eaten[-3:], lambda f: f.name == food.name):
            raise SameFoodException('Same food three days in a row is a no-go')
        if len(self.food_eaten) >= 5 and self.all_match(self.food_eaten[-5:], lambda f: f.type == food.food_type):
            raise SameFoodException('Same type of food for five days, come on!')
        self.tummy_full += food.hunger_points
        self.food_eaten.append(food)
        if self.tummy_full > 100:
            self.tummy_full = 100

    def groom_horse(self):
        self.cleanness += 40
        if self.cleanness > 100:
            self.cleanness = 100

    def all_match(self, iterable: list, function: callable) -> bool:
        for it in iterable:
            if not function(it):
                return False
        return True


class Stables:

    def __init__(self):
        self.rooms = {}
        self.horses = []
        self.food = []

    def add_horse(self, horse: Horse):
        self.horses.append(horse)

    def remove_horse(self, horse: Horse):
        self.horses.remove(horse)

    def get_horses(self):
        return self.horses

    def groom_all_horses(self):
        map(lambda horse: horse.groom(), self.horses)
        # [horse.groom() for horse in self.horses]

    def get_horses_by_color(self, color: str):
        return [horse for horse in self.horses if horse.color == color]
