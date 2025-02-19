from typing import List
from projecttt.equipment.base_equipment import BaseEquipment
from projecttt.equipment.elbow_pad import ElbowPad
from projecttt.equipment.knee_pad import KneePad
from projecttt.teams.base_team import BaseTeam
from projecttt.teams.indoor_team import IndoorTeam
from projecttt.teams.outdoor_team import OutdoorTeam


class Tournament:
    VALID_EQUIPMENT_TYPE = {
        "KneePad": KneePad,
        "ElbowPad": ElbowPad
    }
    VALID_TEAM_TYPE = {
        "OutdoorTeam": OutdoorTeam,
        "IndoorTeam": IndoorTeam
    }

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: List[BaseEquipment] = []
        self.teams: List[BaseTeam] = []


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")

        self.__name = value
    def add_equipment(self, equipment_type: str):
        try:
            equipment = self.VALID_EQUIPMENT_TYPE[equipment_type]()
        except KeyError: # MOJESH DA GO NAPRAWISH KEYERROR
            raise Exception("Invalid equipment type!")

        self.equipment.append(equipment)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        try:
            team = self.VALID_TEAM_TYPE[team_type](team_name, country, advantage)
        except KeyError: # MOJESH DA GO NAPRAWISH KEYERROR
            raise Exception("Invalid team type!")

        if len(self.teams) >= self.capacity:
            return f"Not enough tournament capacity."

        self.teams.append(team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        team = next(filter(lambda t: t.name == team_name, self.teams))
        equipment = next(filter(lambda e: e.__class__.__name__ == equipment_type, reversed(self.equipment))) #TRQBWA DA NAPRAWISH TAKA CHE DA SE WZIMA POSLEDNIQ EQUIPMENT OT TOZI TIP

        if team.budget < equipment.price:
            raise Exception("Budget is not enough!")

        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        try:
            team = next(filter(lambda t: t.name == team_name, self.teams))
        except StopIteration: # MOJESH DA GO NAPRAWISH STOPITERATION
            raise Exception("No such team!")

        if team.wins > 0:
            raise Exception (f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        counter = 0

        for e in self.equipment:
            if e.__class__.__name__ == equipment_type:
                e.increase_price()
                counter += 1

        return f"Successfully changed {counter}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team1 = next(filter(lambda t: t.name == team_name1, self.teams))
        team2 = next(filter(lambda t: t.name == team_name2, self.teams))

        if team1.__class__.__name__ != team2.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")

        t1_points = team1.advantage + sum(e.protection for e in team1.equipment)
        t2_points = team2.advantage + sum(e.protection for e in team2.equipment)

        if t1_points > t2_points:
            team1.win()
            return f"The winner is {team1.name}."

        elif t2_points > t1_points:
            team2.win()
            return f"The winner is {team2.name}."

        return "No winner in this game."

    def get_statistics(self):
        sorted_teams = sorted(self.teams, key=lambda t: -t.wins)
        result = f"Tournament: {self.name}\n" + \
                  "Number of Teams: {len(self.teams)}\n" + \
                  "Teams:\n" + \
                  '\n'.join(t.get_statistics() for t in sorted_teams)

        return result