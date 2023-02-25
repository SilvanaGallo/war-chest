from warchest.unit_cards import BattlefieldUnitCard


class CavalryUnitCard(BattlefieldUnitCard):
    """Cavalry: Cavalry are mobile units that can move and then attack a unit
    ○ It can attack from an adjacent space
    ○ It can move only one orthogonal space at a time, and then they may attack an
    enemy unit if it’s adjacent within the same action
    ○ There are 4 Cavalry units in total"""

    def __init__(self) -> None:
        self.total_units: int = 4
        self.name: str = "Cavalry"

    def __repr__(self) -> str:
        return "C"

    def move_action(self) -> None:
        raise NotImplementedError

    def attack_action(self) -> None:
        raise NotImplementedError
