from typing import List
from project.player import Player


class Guild:

    def __init__(self, name: str):
        self.name = name
        self.players: List[str] = []

    def assign_player(self, player: Player):
        if player in self.players:
            return f"Player {player.name} is already in the guild."

        elif player not in self.players and player.guild == 'Unaffiliated':
            player.guild = self.name
            self.players.append(player)
            return f"Welcome player {player.name} to the guild {self.name}"

        return f"Player {player.name} is in another guild."

    def kick_player(self, player_name: str):
        if player_name in self.players:
            self.players.remove(player_name)
            player_name.guild = 'Unaffiliated'

            return f"Player {player_name} has been removed from the guild."

        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        guild_details = '\n'.join(p.player_info() for p in self.players)

        return f"Guild: {self.name}\n" \
               f"{guild_details}"


guild = Guild("GGXrd")
player = Player("Pesho", 90, 90)
print(guild.assign_player(player))
print(guild.assign_player(player))
