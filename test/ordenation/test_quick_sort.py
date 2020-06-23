import pytest
from algorithms.ordenation import QuickSort


class TestQuickSort:
    @pytest.mark.parametrize("list, number_of_pivots, expected",
                             [
                                 ([1, 2, 3], 1, [1]),
                                 ([1, 2, 3], 2, [1, 2]),
                                 ([1, 2, 3], 3, [1, 2, 3])
                             ])
    def test_get_pivots(self, list, number_of_pivots, expected):
        algo = QuickSort()
        obtained = algo.get_pivots(list, number_of_pivots)
        assert number_of_pivots == len(obtained)
        assert expected == obtained

    @pytest.mark.parametrize("list, number_of_pivots",
                             [
                                 ([], 0),
                                 ([], 1),
                                 ([], 2),
                                 ([7], 2),
                                 ([5, 7], 0)
                             ])
    def test_get_pivots_exception(self, list, number_of_pivots):
        with pytest.raises(Exception):
            algo = QuickSort()
            algo.get_pivots(list, number_of_pivots)

    @pytest.mark.parametrize("list, number_of_pivots, expected",
                             [
                                 ([1, 2, 3], 1, [3]),
                                 ([1, 2, 3], 2, [2, 3]),
                                 ([1, 2, 3], 3, [1, 2, 3])
                             ])
    def test_get_last_as_pivots(self, list, number_of_pivots, expected):
        algo = QuickSort()
        obtained = algo.get_last_as_pivots(list, number_of_pivots)
        assert expected == obtained

    def test_get_random_as_pivots(self):
        list = [191, 2, 73, 1, 7, 3, 5]
        number_of_pivots = 3
        algo = QuickSort()
        obtained = algo.get_random_as_pivots(list, number_of_pivots)

        assert number_of_pivots == len(obtained)

    @pytest.mark.parametrize("list, expected",
                             [
                                 ([1, 2, 3], 2),
                                 ([1, 2, 15, 3], 15),
                                 ([1], 1)
                             ])
    def test_get_middle_as_pivots(self, list, expected):
        algo = QuickSort()
        obtained = algo.get_middle_as_pivot(list)
        assert expected == obtained

    @pytest.mark.parametrize("list, expected",
                             [
                                 ([1, 2, 3], 2),
                                 ([1, 2, 15, 3], 6),
                                 ([8, 2], 5),
                                 ([1], 1),
                                 ([], 0)
                             ])
    def test_get_average_as_pivot(self, list, expected):
        algo = QuickSort()
        obtained = algo.get_average_as_pivot(list)
        assert expected == obtained
