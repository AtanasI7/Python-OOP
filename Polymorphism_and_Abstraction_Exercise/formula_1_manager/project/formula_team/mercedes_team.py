from typing import Dict

from project.formula_team.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):

    @property
    def sponsors(self):
        return {
            "Petronas": {
                1: 1_000_000,
                2: 500_000
            },
            "TeamViewer": {
                5: 100_000,
                7: 50_000
            }
        }
    
    @property
    def expenses_for_one_race(self):
        return 200_000