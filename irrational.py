from __future__ import annotations

class Irrational:
    def __init__(self, formula) -> None:
        from types import FunctionType
        self.dp = 20
        if isinstance(formula, FunctionType):
            self._is_transcendental = True
            self._generator = formula
        elif isinstance(formula, str):
            self._is_transcendental = False
            self._formula = formula

    def _getvalue(self):
        if self._is_transcendental: return self._generator(self.dp)
        from decimal import Decimal, getcontext
        self.dp += 6
        getcontext().prec = self.dp+1
        result = str(eval(self._formula))[:-6]
        self.dp -= 6
        return Decimal(result)


    def __str__(self) -> str:
        return str(self._getvalue()) + '...'

    # Arithmetic operations

    def _calc(self, operator: str, _other: Irrational | int | float):
        if self._is_transcendental:
            def gen_result(digits):
                if _other._is_transcendental:
                    return f"Decimal('{self._generator(digits)}') {operator} Decimal('{_other._generator(digits)}')"
                else:
                    return f"Decimal('{self._generator(digits)}') {operator} ({_other._formula})"
            result = gen_result(self.dp)
        else:
            if isinstance(_other, Irrational):
                formula = f"({self._formula}) {operator} ({_other._formula})"
            elif isinstance(_other, int) or isinstance(_other, float):
                formula = f"({self._formula}) {operator} ({_other})"
            else:
                return NotImplemented
            result = formula
        return Irrational(result)

    def _rcalc(self, operator: str, _other: Irrational | int | float):
        if self._is_transcendental:
            def gen_result(digits):
                if _other._is_transcendental:
                    return f"Decimal('{_other._generator(digits)}') {operator} Decimal('{self._generator(digits)}')"
                else:
                    return f"({_other._formula}) {operator} Decimal('{self._generator(digits)}')"
            result = gen_result(self.dp)
        else:
            if isinstance(_other, Irrational):
                formula = f"({_other._formula}) {operator} ({self._formula})"
            elif isinstance(_other, int) or isinstance(_other, float):
                formula = f"({_other}) {operator} ({self._formula})"
            else:
                return NotImplemented
            result = formula
        return Irrational(result)

    def __add__(self, _other) -> Irrational:
        return self._calc('+', _other)
    
    def __radd__(self, _other) -> Irrational:
        return self._rcalc('+', _other)

    def __sub__(self, _other) -> Irrational:
        return self._calc('-', _other)

    def __rsub__(self, _other) -> Irrational:
        return self._rcalc('-', _other)

    def __mul__(self, _other) -> Irrational:
        return self._calc('*', _other)

    def __rmul__(self, _other) -> Irrational:
        return self._rcalc('*', _other)

    def __truediv__(self, _other) -> Irrational:
        return self._calc('/', _other)
    
    def __rtruediv__(self, _other) -> Irrational:
        return self._rcalc('/', _other)
    
    #def __floordiv__(self, _other) -> int:
    #    return self._calc('//', _other)

    #def __rfloordiv__(self, _other) -> int:
    #    return self._rcalc('//', _other)

    def __mod__(self, _other) -> Irrational:
        return self._calc('%', _other)

    def __rmod__(self, _other) -> Irrational:
        return self._rcalc('%', _other)

    def __divmod__(self, _other) -> Irrational:
        return self._calc('//', _other), self._calc('%', _other)

    def __rdivmod__(self, _other) -> Irrational:
        return self._rcalc('//', _other), self._rcalc('%', _other)

    def __pow__(self, _other) -> Irrational:
        return self._calc('**', _other)

    def __rpow__(self, _other) -> Irrational:
        return self._rcalc('**', _other)

def nroot(rt, value) -> Irrational | int:
    floor_root = int(pow(value, 1/rt))
    perfect_square = lambda: floor_root**rt == value

    if not perfect_square():
        return Irrational(f"pow(Decimal('{value}'), (1/Decimal('{rt}')))")
    else:
        return Irrational(f"{floor_root}")

def _gen_pi(digits):
    if digits == 0: return '3'
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    counter = 0
    pi_digits = ''
    while counter != (digits + 1):
        if 4 * q + r - t < n * t:
            pi_digits += str(n)
            if counter == 0:
                pi_digits += '.'
            counter += 1
            nr = 10 * (r - n * t)
            n = ((10 * (3 * q + r)) // t) - 10 * n
            q *= 10
            r = nr
        else:
            nr = (2 * q + r) * l
            nn = (q * (7 * k) + 2 + (r * l)) // (t * l)
            q *= k
            t *= l
            l += 2
            k += 1
            n = nn
            r = nr
    return pi_digits
pi = Irrational(_gen_pi)
if __name__ == "__main__":
    pi = Irrational(_gen_pi)
    print(pi - 3)
