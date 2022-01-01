from pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemo: Pokemon):
        if pokemo in self.pokemons:
            return 'This pokemon is already caught'

        self.pokemons.append(pokemo)
        return f'Caught {pokemo.pokemon_details()}'

    def release_pokemon(self, pokemon_name: str):
        check = list(filter(lambda a: a.name == pokemon_name, self.pokemons))

        if check:
            pokemo = check[0]
            self.pokemons.remove(pokemo)
            return f'You have released {pokemon_name}'

        return 'Pokemon is not caught'

    def trainer_data(self):
        output_list = [
            f'Pokemon Trainer {self.name}',
            f'Pokemon count {len(self.pokemons)}'
        ]

        for pokemon in self.pokemons:
            output_list.append(f'- {pokemon.pokemon_details()}')

        return '\n'.join(output_list)
