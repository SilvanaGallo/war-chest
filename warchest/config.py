from warchest.unit_cards import ArcherUnitCard, BerserkerUnitCard, CavalryUnitCard, CrossbowmanUnitCard, \
                                KnightUnitCard, LancerUnitCard, MercenaryUnitCard, SwordsmanUnitCard
class Config:
    
    HAND_SIZE: int = 3
    
    ACTIONS: list[str] = ['move', 'recruit', 'place', 'attack', 'control', 'initiative', 'forfeit']

    UNITS: dict[str] = {    0: ArcherUnitCard,
                            1: BerserkerUnitCard,
                            2: CavalryUnitCard,
                            3: CrossbowmanUnitCard,
                            4: KnightUnitCard,
                            5: LancerUnitCard,
                            6: MercenaryUnitCard,
                            7: SwordsmanUnitCard }
    