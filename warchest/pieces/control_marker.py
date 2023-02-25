

class ControlMarker:

    def __init__(self, owner_name: str) -> None:
        self.owner_name: str = owner_name

    def __repr__(self) -> str:
        return f"{self.owner_name[0]} "