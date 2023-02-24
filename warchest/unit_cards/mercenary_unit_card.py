from warchest.unit_cards import BattlefieldUnitCard

class MercenaryUnitCard(BattlefieldUnitCard):

    def __init__(self) -> None:
        self.total_units: int = 5

    def __repr__(self) -> str:
        return 'M'

    def attack(self) -> None:
        raise NotImplementedError

    def attack(self) -> None:
        raise NotImplementedError