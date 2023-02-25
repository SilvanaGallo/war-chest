from warchest.unit_cards import BattlefieldUnitCard


class KnightUnitCard(BattlefieldUnitCard):
    """Knight: Knights are one of the standard units that has no abilities, just to make the
    game balanced
    ○ It can attack from an adjacent space
    ○ It can move only one orthogonal space at a time
    ○ There are 5 Knights units in total"""

    def __init__(self) -> None:
        self.total_units: int = 5
        self.name: str = "Knight"

    def __repr__(self) -> str:
        return "K"

    def attack(self) -> None:
        raise NotImplementedError

    def attack(self) -> None:
        raise NotImplementedError
