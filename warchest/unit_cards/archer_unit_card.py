from . import BattlefieldUnitCard


class ArcherUnitCard(BattlefieldUnitCard):
    """Archer: Archers are versatile units that can attack from a distance.
    ○ It can attack from 2 spaces, this also means diagonally
    ○ It can move only one orthogonal space at a time
    ○ There are 4 Archers units in total"""

    def __init__(self) -> None:
        self.total_units: int = 4
        self.name: str = "Archer"

    def __str__(self) -> str:
        return "A"

    def move_action(self) -> None:
        return True

    def attack_action(self) -> None:
        return True
