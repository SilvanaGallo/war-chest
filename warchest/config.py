from warchest.unit_cards import (
    ArcherUnitCard,
    BerserkerUnitCard,
    CavalryUnitCard,
    CrossbowmanUnitCard,
    KnightUnitCard,
    LancerUnitCard,
    MercenaryUnitCard,
    SwordsmanUnitCard,
)


class Config:
    HAND_SIZE: int = 3

    ACTIONS: list[str] = [
        "move",
        "recruit",
        "place",
        "attack",
        "control",
        "initiative",
        "forfeit",
    ]

    UNITS: list[str] = [
        ArcherUnitCard,
        BerserkerUnitCard,
        CavalryUnitCard,
        CrossbowmanUnitCard,
        KnightUnitCard,
        LancerUnitCard,
        MercenaryUnitCard,
        SwordsmanUnitCard,
    ]
