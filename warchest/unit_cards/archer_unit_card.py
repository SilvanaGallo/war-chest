
from warchest.unit_cards import BattlefieldUnitCard


class ArcherUnitCard(BattlefieldUnitCard):

    def __init__(self) -> None:
        self.total_units: int = 4
        self.name: str = 'Archer'

    def __repr__(self) -> str:
        return 'A'

    def attack(self) -> None:
        return True