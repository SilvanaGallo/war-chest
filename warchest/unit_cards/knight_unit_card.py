from warchest.unit_cards import BattlefieldUnitCard

class KnightUnitCard(BattlefieldUnitCard):

    def __init__(self) -> None:
        self.total_units: int = 5
        self.name: str = 'Knight'

    def __repr__(self) -> str:
        return 'K'

    def attack(self) -> None:
        raise NotImplementedError

    def attack(self) -> None:
        raise NotImplementedError