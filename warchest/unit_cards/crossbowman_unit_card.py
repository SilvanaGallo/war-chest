from warchest.unit_cards import BattlefieldUnitCard


class CrossbowmanUnitCard(BattlefieldUnitCard):
    """Crossbowman: Crossbowmans are like archers but they can only attack in straight line
    ○ It can attack from 2 spaces in straight line
    ○ It can move only one orthogonal space at a time
    ○ There are 5 Crossbowman units in total"""

    def __init__(self) -> None:
        self.total_units: int = 5
        self.name: str = "Crossbowman"

    def __str__(self) -> str:
        return "X"

    def move_action(self) -> None:
        raise NotImplementedError

    def attack_action(self) -> None:
        raise NotImplementedError
