from warchest.unit_cards import BattlefieldUnitCard

class LancerUnitCard(BattlefieldUnitCard):

    def __init__(self) -> None:
        self.total_units: int = 4
        self.name: str = 'Lancer'

    def __repr__(self) -> str:
        return 'L'

    def attack(self) -> None:
        raise NotImplementedError

    def attack(self) -> None:
        raise NotImplementedError