from projecttt.teams.base_team import BaseTeam


class OutdoorTeam(BaseTeam):
    INITIAL_BUDGET = 1000.0

    def __init__(self, name: str, country: str, advantage: int):
        BaseTeam.__init__(self, name, country, advantage, self.INITIAL_BUDGET)

    def win(self):
        self.advantage += 115
        self.wins += 1