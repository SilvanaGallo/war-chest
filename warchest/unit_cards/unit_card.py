from abc import ABC, abstractmethod

class UnitCard(ABC):

    def total_units(self) -> int:
        return self.total_units

    @abstractmethod
    def attack(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def attack(self) -> None:
        raise NotImplementedError