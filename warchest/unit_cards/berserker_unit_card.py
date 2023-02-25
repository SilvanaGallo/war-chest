from warchest.unit_cards import BattlefieldUnitCard


class BerserkerUnitCard(BattlefieldUnitCard):
    """Berserker: Berserkers are units that feel the intense battle, so they can attack up to 2
    times with one attack action:
    ○ It can attack up to 2 times with one attack action
    ○ It can move only one orthogonal space at a time
    ○ There are 4 Berserker units in total"""

    def __init__(self) -> None:
        self.total_units: int = 4
        self.name: str = "Berserker"

    def __str__(self) -> str:
        return "B"

    def move_action(self) -> None:
        raise NotImplementedError

    def attack_action(self) -> None:
        raise NotImplementedError
