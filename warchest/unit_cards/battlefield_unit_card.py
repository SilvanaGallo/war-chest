from warchest.unit_cards import UnitCard


class BattlefieldUnitCard(UnitCard):
    def __repr__(self) -> str:
        raise NotImplementedError

    def attack_action(self) -> None:
        raise NotImplementedError

    def recruit_action(self) -> str:
        return "recruit_battlefield"

    def place_action(self) -> str:
        raise "place"
