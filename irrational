from __future__ import annotations
from decimal import Decimal, getcontext

class Irrational:
    def __init__(self, formula) -> None:
        self.dp = 20
        # dp = decimal places
        self._formula = formula
    
    def _getvalue(self):
            self.dp += 6
            getcontext().prec = self.dp+1
            result = str(eval(self._formula))[:-6]
            self.dp -= 6
            return Decimal(result)

    def __str__(self) -> str:
        return str(self._getvalue()) + '...'

    def __add__(self, _other: Irrational | int) -> Irrational:
        if isinstance(_other, Irrational):
            result = f"({self._formula}) + ({_other._formula})"
            return Irrational(result)
        elif isinstance(_other, int):
            result = f"({self._formula}) + ({_other})"
            return Irrational(result)
