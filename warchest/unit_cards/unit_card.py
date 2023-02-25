from typing import Optional
from abc import ABC, abstractmethod
from warchest.pieces import Coin


class UnitCard(ABC):

    def total_units(self) -> int:
        return self.total_units

    def get_name(self) -> str:
        return self.name

    # @abstractmethod
    # def attack(self) -> None:
    #     raise NotImplementedError

    def recruit_unit(self) -> Optional[Coin]:
        if self.total_units > 0:
            self.total_units -= 1
            return Coin(unit_card=self)
        else:
            return None