from abc import ABC, abstractmethod

class UnitCard(ABC):

    @abstractmethod
    def __repr__(self) -> str:
        raise NotImplementedError

    def total_units(self) -> int:
        return self.total_units

    @abstractmethod
    def attack(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def attack(self) -> None:
        raise NotImplementedError