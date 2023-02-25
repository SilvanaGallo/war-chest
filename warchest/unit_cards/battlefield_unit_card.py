from abc import abstractmethod
from warchest.unit_cards import UnitCard


class BattlefieldUnitCard(UnitCard):
    def __str__(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def move_action(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def attack_action(self) -> None:
        raise NotImplementedError

    def recruit_action(self) -> str:
        return "recruit_battlefield"

    def place_action(self) -> str:
        raise "place"

    def control_action(self) -> str:
        raise "control"
