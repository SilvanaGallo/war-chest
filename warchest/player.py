from warchest.unit_cards import UnitCard

class Player:

    def __init__(self, name: str) -> None:
        self.name = name
        self.recruitment: list[UnitCard] = []
        self.bag: list[Coin] = []
        self.discard_stack: list[Coin] = []
        self.hand: list[Coin] = []
        
        
        