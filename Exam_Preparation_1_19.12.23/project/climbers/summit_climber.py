from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):
    STRENGTH_REDUCE_ADVANCED = 30 * 1.3
    STRENGTH_REDUCE_EXTREME = 30 * 2.5
    MIN_STRENGTH_NEEDED = 75
    INITIAL_STRENGTH = 150

    def __init__(self, name: str):
        BaseClimber.__init__(self, name, SummitClimber.INITIAL_STRENGTH)

    def can_climb(self) -> bool:
        return self.strength >= SummitClimber.MIN_STRENGTH_NEEDED

    def climb(self, peak: BasePeak) -> None:
        if peak.difficulty_level == "Advanced":
            self.strength -= SummitClimber.STRENGTH_REDUCE_ADVANCED

        else:
            self.strength -= SummitClimber.STRENGTH_REDUCE_EXTREME

        self.conquered_peaks.append(peak.name)