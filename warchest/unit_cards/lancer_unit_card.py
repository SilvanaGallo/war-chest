from warchest.unit_cards import BattlefieldUnitCard


class LancerUnitCard(BattlefieldUnitCard):
    """Lancer: Lancers are ground, high reach units. They can move one or 2 spaces and then
    attack, but they can only attach IF they move:
    ○ It can attack from an adjacent space but only if previously they moved first as an action
    ○ It can move 1 or 2 spaces
    ○ There are only 4 Lancers units in total"""

    def __init__(self) -> None:
        self.total_units: int = 4
        self.name: str = "Lancer"

    def __str__(self) -> str:
        return "L"

    def move_action(self) -> None:
        raise NotImplementedError

    def attack_action(self) -> None:
        raise NotImplementedError
