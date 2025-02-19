from projecttt.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    KNEE_PROTECTION: int = 120
    KNEE_PROTECTION_PRICE: float = 15.0


    def __init__(self):
        BaseEquipment.__init__(self, self.KNEE_PROTECTION, self.KNEE_PROTECTION_PRICE)

    def increase_price(self):
        self.KNEE_PROTECTION_PRICE += self.KNEE_PROTECTION_PRICE * 0.2
