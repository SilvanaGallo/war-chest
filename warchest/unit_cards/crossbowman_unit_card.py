from warchest.unit_cards import Battlefield

class CrossbowmanUnitCard(Battlefield):

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