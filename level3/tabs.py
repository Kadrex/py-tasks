"""Poke stuff here."""


class Characteristic:

    def __init__(self):
        self.color = ""
        self.item = ""
        self.size = 0


class Pokemon:

    def __init__(self):
        self.name = ""
        self.characteristics = []

    def change_name(self, new_name):
        self.name = new_name

    def add_characteristic(self):
        self.characteristics.append([])

    def remove_characteristic(self, characteristic_index: int):
        self.characteristics.remove(characteristic_index)


class PokemonView:

    def __init__(self):
        self.pokemon = []
        self.characteristics_view = PokemonCharacteristicView()

    def click_add_pokemon(self):
        self.pokemon.append(Pokemon())

    def on_pokemon_name_change(self, pokemon_index: int, name: str):
        self.pokemon[pokemon_index].change_name(name)

    def click_remove_pokemon(self, pokemon_index: int):
        self.pokemon.remove(pokemon_index)


class PokemonCharacteristicView:

    def __init__(self, pokemon: list):
        self.active_pokemon_index = 0
        self.pokemon = pokemon

    def click_another_pokemon_tab(self, tab_index: int):
        self.active_pokemon_index = tab_index

    def click_add_characteristic(self):
        self.pokemon[self.active_pokemon_index].add_characteristic(Characteristic())

    def click_remove_characteristic(self, characteristic_index):
        pass
