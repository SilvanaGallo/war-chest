from warchest.unit_cards import BattlefieldUnitCard

class SwordsmanUnitCard(BattlefieldUnitCard):

    def __init__(self) -> None:
        self.total_units: int = 4
        self.name: str = 'Swordsman'

    def __repr__(self) -> str:
        return 'S'

    def attack(self) -> None:
        raise NotImplementedError

    def attack(self) -> None:
        raise NotImplementedError