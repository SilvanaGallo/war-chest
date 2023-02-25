from typing import Optional
from warchest.unit_cards import UnitCard
from warchest.pieces import Coin

class BattlefieldUnitCard(UnitCard):

    def __repr__(self) -> str:
        raise NotImplementedError

    def attack(self) -> None:
        raise NotImplementedError

