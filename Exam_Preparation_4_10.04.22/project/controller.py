from typing import List, Tuple
from project.player import Player
from project.supply.drink import Drink
from project.supply.food import Food
from project.supply.supply import Supply


class Controller:
    VALID_SUSTENANCE = [
        "Food",
        "Drink"
    ]


    def __init__(self):
        self.players: List[Player] = []
        self.supplies: List[Supply] = []

    def add_player(self, *players: Tuple[Player]):
        players_added = []

        for p in players:
            if p not in self.players:
                self.players.append(p)
                players_added.append(p.name)

        return f"Successfully added: {', '.join(players_added)}"

    def add_supply(self, *supplies: Tuple[Supply]):
        for s in supplies:
            self.supplies.append(s)

    def sustain(self, player_name: str, sustenance_type: str):
        try:
            player = next(filter(lambda p: p.name == player_name, self.players))
        except StopIteration:
            return

        if sustenance_type not in Controller.VALID_SUSTENANCE:
            return

        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        # for i in range(len(self.supplies) - 1, -1, -1):
        #     supply = self.supplies[i]
        #
        #     if supply.__class__.__name__ == sustenance_type:
        #         self.supplies.pop(i)
        #         break
        # else:
        #     raise Exception(f"There are no {sustenance_type.lower()} supplies left!")
        #
        # if player.stamina + supply.energy > 100:
        #     player.stamina = 100
        # else:
        #     player.stamina += supply.energy
        #
        # return f"{player_name} sustained successfully with {supply.name}."

        try:
            supply = next(filter(lambda s: s.__class__.__name__ == sustenance_type, reversed(self.supplies)))
        except StopIteration:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")
        if player.stamina + supply.energy <= 100:
            self.supplies.remove(supply)
            player.stamina += supply.energy

            return f"{player_name} sustained successfully with {supply.name}."

        if player.stamina + supply.energy > 100:
            player.stamina = 100

    def duel(self, first_player_name: str, second_player_name: str):
        current_players = sorted([
            next(filter(lambda p: p.name == first_player_name, self.players)),
            next(filter(lambda p: p.name == second_player_name, self.players))
        ], key=lambda p: p.stamina)

        errors_list = []

        for player in current_players:
            if player.stamina <= 0:
                errors_list.append(f"Player {player.name} does not have enough stamina.")

        if errors_list:
            return "\n".join(errors_list)

        return self.fight(current_players)

    def fight(self, current_players: List[Player]):
        first_player_damage = current_players[0].stamina / 2
        current_players[1].stamina = max(current_players[1].stamina - first_player_damage, 0)

        second_player_damage = current_players[1].stamina / 2
        current_players[0].stamina = max(current_players[0].stamina - second_player_damage, 0)

        if current_players[0].stamina <= second_player_damage:
            current_players[0].stamina = 0
        else:
            current_players[0].stamina -= second_player_damage

        winner = sorted(current_players, key=lambda p: -p.stamina)[0]

        return f"Winner: {winner.name}"

    def next_day(self):
        for p in self.players:
            reduce_stamina_with = p.age * 2
            p.stamina = min(p.stamina - reduce_stamina_with, 0)

            self.sustain(p.name, "Food")
            self.sustain(p.name, "Drink")

    def __str__(self):
        players_result = []
        # supplies_result = []

        for player in self.players:
            players_result.append(str(player))

        for supply in self.supplies:
            players_result.append(supply.details())

        return "\n".join(players_result)






















