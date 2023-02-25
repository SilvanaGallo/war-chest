from typing import Optional
from warchest.unit_cards import UnitCard
from warchest.pieces import Coin


class BattlefieldUnitCard(UnitCard):
    def __repr__(self) -> str:
        raise NotImplementedError

    def attack_action(self) -> None:
        raise NotImplementedError

    def recruit_action(self) -> str:
        return f"recruit_battlefield"
    
    def place_action(self) -> str:
        raise 'place'
