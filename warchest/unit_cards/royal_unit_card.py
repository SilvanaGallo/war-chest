from typing import Optional
from warchest.unit_cards import UnitCard
from warchest.pieces import Coin

class RoyalUnitCard(UnitCard):

    def __init__(self) -> None:
        self.total_units: int = 1
        self.name: str = 'Royal'

    def get_initiative(self): None

    def recruit_unit(self) -> Optional[Coin]:
        if self.total_units > 0:
            self.total_units -= 1
            return Coin(unit_card=self)
        else:
            return None
