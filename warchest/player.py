from warchest import UnitCard

class Player:

    def __init__(self, name: str) -> None:
        self.name = name
        self.unit_cards: list[UnitCard] = []
        self.bag: list[Coin] = []
        self.discard_stack: list[Coin] = []
        self.hand: list[Coin] = []
        
        
        