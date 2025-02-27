from projecttttt.fish.base_fish import BaseFish


class DeepSeaFish(BaseFish):
    TIME_TO_CATCH = 180

    def __init__(self, name: str, points: float):
        BaseFish.__init__(self, name, points, self.TIME_TO_CATCH)

    def fish_details(self):
        return (f"{self.__class__.__name__}: {self.name} "
                f"[Points: {self.points}, "
                f"Time to Catch: {self.time_to_catch} seconds]")