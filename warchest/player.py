from warchest.unit_cards import UnitCard

class Player:

    def __init__(self, name: str, symbol: str) -> None:
        self.name: str = name
        self.symbol: str = symbol
        self.initiative: bool = False
        self.recruitment: list[UnitCard] = []
        self.bag: list[Coin] = []
        self.discard_stack: list[Coin] = []
        self.hand: list[Coin] = []
        
    def set_initiative(self):
        self.initiative = True
    
    def unset_initiative(self):
        self.initiative = False
        
        