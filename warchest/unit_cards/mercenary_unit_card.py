from warchest.unit_cards import BattlefieldUnitCard


class MercenaryUnitCard(BattlefieldUnitCard):
    """Mercenary: Mercenaries are the other unit type that has no abilities
    ○ It can attack from an adjacent space
    ○ It can move only one orthogonal space at a time
    ○ There are 5 Mercenaries units in total"""

    def __init__(self) -> None:
        self.total_units: int = 5
        self.name: str = "Mercenary"

    def __repr__(self) -> str:
        return "M"

    def attack_action(self) -> None:
        raise NotImplementedError

    def move_action(self) -> None:
        raise NotImplementedError
