import random
from warchest.unit_cards import BattlefieldUnitCard, RoyalUnitCard
from warchest.pieces import Coin


class Player:
    def __init__(self, name: str, symbol: str) -> None:
        self.name: str = name
        self.symbol: str = symbol
        self.initiative: bool = False
        self.recruitment: dict[str, BattlefieldUnitCard] = {}
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
        self.recruitment[uc.get_name()] = uc

    def fill_bag(self) -> None:
        # add unit coins to bag
        for v in self.recruitment.values():
            for i in range(2):
                unit: Coin = v.recruit_unit()
                unit.set_owner_symbol(self.symbol)
                self.bag.append(unit)
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
            random_coin: int = random.randint(0, len(self.bag) - 1)
            self.hand.append(self.bag.pop(random_coin))

    def get_coin_from_hand(self, type: str) -> Coin:
        matches: list = [
            i for i, x in enumerate(self.hand) if x.get_unit_type() == type
        ]
        index: int = matches[0]
        coin: Coin = self.hand.pop(index)
        return coin

    def has_coins_in_hand(self) -> bool:
        return len(self.hand) > 0

    def discard(self, type: str) -> Coin:
        discarded: Coin = self.get_coin_from_hand(type)
        self.discard_stack.append(discarded)
        return discarded

    def recruit_unit(self, type: str) -> bool:
        if type in self.recruitment:
            coin: Coin = self.recruitment[type].recruit_unit()
            coin.set_owner_symbol(self.symbol)
            if coin:
                self.bag.append(coin)
                return True
            else:
                return False

    def hand_string(self) -> str:
        hand_str: str = "Hand: "
        for h in self.hand:
            hand_str += f"{h.unit_card.name}, "
        return hand_str + "\n"

    def recruitment_string(self) -> str:
        recruitment_str: str = "Recruitment pieces: "
        for e in self.recruitment.values():
            recruitment_str += f"{e.name} = {e.total_units}, "
        return recruitment_str + "\n"

    def discard_string(self) -> str:
        discard_str: str = "Discard pile: "
        for e in self.discard_stack:
            discard_str += f"{e.unit_card.name}, "
        return discard_str + "\n"

    def __str__(self) -> str:
        output: str = f"========= {self.name} ({self.symbol}) ========= \n"

        return (
            output
            + self.hand_string()
            + self.recruitment_string()
            + self.discard_string()
            + f"Control tokens: {self.remaining_tokens} \n"
        )
