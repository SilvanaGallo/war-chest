from warchest.unit_cards import BattlefieldUnitCard

class CavalryUnitCard(BattlefieldUnitCard):

    def __init__(self) -> None:
        self.total_units: int = 4
        self.name: str = 'Cavalry'

    def __repr__(self) -> str:
       return 'C'

    def attack(self) -> None:
        raise NotImplementedError

    def attack(self) -> None:
        raise NotImplementedError