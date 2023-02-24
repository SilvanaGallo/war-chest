from warchest.unit_cards import UnitCard

class RoyalUnitCard(UnitCard):

    def __init__(self) -> None:
        self.total_units: int = 2

    def attack(self) -> None:
        raise NotImplementedError

    def attack(self) -> None:
        raise NotImplementedError