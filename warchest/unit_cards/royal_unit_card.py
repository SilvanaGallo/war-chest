from typing import Optional
from warchest.unit_cards import UnitCard
from warchest.pieces import Coin


class RoyalUnitCard(UnitCard):
    """Royal: The royalty doesn’t go into the battlefield, but it can
    influence your initiative or recruit other units. There is 1 Royal
    unit per player in their bag at the start of the game, so they never
    get deleted from the game.
    ○ They only can be used to recruit or get the initiative
    ○ There are 2 Royal units in total, 1 per player"""

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(RoyalUnitCard, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        self.total_units: int = 1
        self.name: str = "Royal"

    def recruit_unit(self) -> Optional[Coin]:
        if self.total_units > 0:
            self.total_units -= 1
            return Coin(unit_card=self)
        else:
            return None

    def recruit_action(self) -> str:
        return "recruit_royal"

    def place_action(self) -> str:
        raise NotImplementedError
