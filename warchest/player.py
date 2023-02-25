import random
from warchest.unit_cards import BattlefieldUnitCard, RoyalUnitCard
from warchest.pieces import Coin

class Player:

    def __init__(self, name: str, symbol: str) -> None:
        self.name: str = name
        self.symbol: str = symbol
        self.initiative: bool = False
        self.recruitment: list[BattlefieldUnitCard] = []
        self.bag: list[Coin] = []
        self.discard_stack: list[Coin] = []
        self.hand: list[Coin] = []
        self.remaining_tokens: int = 4
        
    def is_winner(self) -> bool:
        return self.remaining_tokens == 0

    def has_initiative(self) -> bool:
        return self.initiative

    def set_initiative(self) -> None:
        self.initiative = True
    
    def unset_initiative(self) -> None:
        self.initiative = False

    def add_unit_card(self, uc: BattlefieldUnitCard) -> None:
        self.recruitment.append(uc)

    def fill_bag(self) -> None:
        # add unit coins to bag
        for u in self.recruitment:
            for i in range(2):
                self.bag.append(u.recruit_unit())
        
        # add royal coin
        self.bag.append(RoyalUnitCard().recruit_unit())

    def add_discarded_units(self) -> None:
        while self.discard_stack:
            self.bag.append(self.discard_stack.pop())   

    def get_hand(self, hand_size: int) -> None:
        if len(self.bag) < hand_size:
            self.add_discarded_units()
        # select random coins
        for i in range(hand_size):
            random_coin: int = random.randint(0, len(self.bag)-1)
            self.hand.append(self.bag.pop(random_coin))   

    def has_coins_in_hand(self) -> bool:
        return len(self.hand) > 0

    def discard(self, type: str) -> None:
        matches: list = [i for i, x in enumerate(self.hand) if x.get_unit_type() == type]
        index: int = matches[0]
        discarded: Coin = self.hand.pop(index)
        self.discard_stack.append(discarded)
        return discarded

    def hand_string(self) -> str:
        hand_str: str = 'Hand: '
        for h in self.hand:
            hand_str += f'{h.unit_card.name}, '
        return hand_str+'\n'

    def recruitment_string(self) -> str:
        recruitment_str: str = 'Recruitment pieces: '
        for e in self.recruitment:
            recruitment_str += f'{e.name} = {e.total_units}, '
        return recruitment_str +'\n'
        
    def discard_string(self) -> str:
        discard_str: str = 'Discard pile: '
        for e in self.discard_stack:
            discard_str += f'{e.unit_card.name}, '
        return discard_str +'\n'
                  
        
    def __repr__(self) -> str:
        output: str = f'========= {self.name} ({self.symbol}) ========= \n'
        
        return output + self.hand_string() + self.recruitment_string() + self.discard_string() + f'Control tokens: {self.remaining_tokens} \n'

        
        