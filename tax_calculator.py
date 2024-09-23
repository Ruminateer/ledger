from collections.abc import Iterable
from typing import NamedTuple


class Bracket(NamedTuple):
    end: float
    rate: float


class Tax:
    def __init__(self, brackets: Iterable[Bracket]) -> None:
        self._brackets = sorted(brackets)

    def calculate(self, amount: float, begin: float = 0) -> float:
        total_tax = 0
        for brkt in self._brackets:
            taxable_in_bracket = min(brkt.end - begin, amount)
            total_tax += taxable_in_bracket * brkt.rate
            amount -= taxable_in_bracket
            begin = brkt.end
        return total_tax
