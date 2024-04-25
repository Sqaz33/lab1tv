from math import factorial as fact


class Combinatorics:
    def combinations(self, n: int, k: int) -> int:
        """
        :param n: количество элементов в множестве
        :param k: количество элементов в сочетании
        :return: количество сочетаний
        """
        return fact(n) // (fact(k) * fact(n - k))

    def partial_permut(self, n: int, k: int) -> int:
        """
        :param n: количество элементов в множестве
        :param k: количество элементов в размещении
        :return: количетсво размещений
        """
        return fact(n) // fact(n - k)

    def partial_permut_rep(self, n: int, k: int) -> int:
        """
        :param n: количество элементов в множестве
        :param k: количество элементов в размещении
        :return: количество размещений с повторениями
        """
        return n ** k

    def permutation_rep(self, count: [int, ...]) -> int:
        """
        :param multiple: множество чисел
        :return: количество перестановаок
        """

        denom = 1
        for c in count:
            denom *= fact(c)

        return fact(sum(count)) // denom

