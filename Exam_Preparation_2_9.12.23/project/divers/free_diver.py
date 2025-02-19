from projecttttt.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    INITIAL_OXYGEN_LEVEL = 120

    def __init__(self, name: str):
        BaseDiver.__init__(self, name, FreeDiver.INITIAL_OXYGEN_LEVEL)

    def miss(self, time_to_catch: int):
        reduced_amount = round(time_to_catch * 0.6)

        if self.oxygen_level < reduced_amount:
            self.oxygen_level = 0
        else:
            self.oxygen_level -= reduced_amount


    def renew_oxy(self):
        self.oxygen_level = FreeDiver.INITIAL_OXYGEN_LEVEL