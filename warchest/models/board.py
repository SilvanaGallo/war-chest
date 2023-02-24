from typing import Optional, Dict, Tuple
from warchest.models import Unit

class Board:

    def __init__(self, size: int = 9)-> None:
        self.n: int = size
        self.content: Dict[Tuple[str, int], Optional[Unit]] = {}

    def setup(self) -> None:
        
        for x in range(self.n):
            for y in range(self.n):
                pass

    def _string_column(self, index: int) -> chr:
        return chr(ord('a') + index)

    def print(self) -> None:
        # print header
        header: str = ' '
        divisor: str = ' '
        for i in range(self.n):
            header += '  ' + self._string_column(i)
            divisor += '---'
        print(header)
        print(divisor)

        # print content
        for row in range(self.n):
            output: str = f'{row}|'
            for col in range(self.n):
                key_obj: tuple = (self._string_column(row), col)
                output += ' ' + (self.content[key_obj] if key_obj in self.content else '. ')
            print(output)

