from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):
    REDUCED_STRENGTH_EXTREME = 20 * 2
    REDUCED_STRENGTH_ADVANCED = 20 * 1.5
    MIN_STRENGTH_NEEDED: int = 100
    INITIAL_STRENGTH: float = 200

    def __init__(self, name: str):
        BaseClimber.__init__(self, name, ArcticClimber.INITIAL_STRENGTH)

    def can_climb(self) -> bool:
        return self.strength >= ArcticClimber.MIN_STRENGTH_NEEDED

    def climb(self, peak: BasePeak) -> None:
        if peak.difficulty_level == 'Extreme':
            self.strength -= ArcticClimber.REDUCED_STRENGTH_EXTREME

        else:
            self.strength -= ArcticClimber.REDUCED_STRENGTH_ADVANCED

        self.conquered_peaks.append(peak.name)