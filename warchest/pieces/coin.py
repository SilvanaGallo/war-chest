class Coin:

    def __init__(self, unit_card) -> None:
        self.unit_card = unit_card
        self.owner_symbol: str = ''

    def set_owner_symbol(self, owner_symbol: str) -> None:
        self.owner_symbol = owner_symbol

    def get_unit_type(self) -> str:
        return self.unit_card.name

    def __repr__(self) -> str:
        return f"{self.unit_card}{self.owner_symbol}"