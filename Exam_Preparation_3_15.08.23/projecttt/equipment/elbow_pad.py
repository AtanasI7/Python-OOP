from projecttt.equipment.base_equipment import BaseEquipment


class ElbowPad(BaseEquipment):
    ELBOW_PROTECTION: int = 90
    ELBOW_PROTECTION_PRICE: float = 25.0

    def __init__(self):
        BaseEquipment.__init__(self, self.ELBOW_PROTECTION, self.ELBOW_PROTECTION_PRICE)

    def increase_price(self):
        self.ELBOW_PROTECTION_PRICE += self.ELBOW_PROTECTION_PRICE * 0.1