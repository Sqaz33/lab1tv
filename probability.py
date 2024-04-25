import combinatorics

# не работает!!!
class Probability:
    def __init__(self):
        self.comb = combinatorics.Combinatorics()

    def calculate(self, n: int, m: int) -> float:
        return self.comb.partial_permut(n, m) / self.comb.partial_permut_rep(n, m)
