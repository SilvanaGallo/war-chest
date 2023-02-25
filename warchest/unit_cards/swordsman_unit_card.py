from warchest.unit_cards import BattlefieldUnitCard


class SwordsmanUnitCard(BattlefieldUnitCard):
    """Swordsman: Swordsman are the opposite of Cavalry, after they attack they can move
    one space
    ○ It can attack from an adjacent space and then they may move within the same action
    ○ It can move only one orthogonal space at a time
    ○ There are 4 Swordsman units in total"""

    def __init__(self) -> None:
        self.total_units: int = 4
        self.name: str = "Swordsman"

    def __repr__(self) -> str:
        return "S"

    def move_action(self) -> None:
        raise NotImplementedError

    def attack_action(self) -> None:
        raise NotImplementedError
