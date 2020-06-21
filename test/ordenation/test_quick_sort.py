import pytest
from algorithms.ordenation import QuickSort

class TestQuickSort:
    @pytest.mark.parametrize("list, number_of_pivots",
        [
            ([], 0),
            ([], 2),
            ([7], 0),
            ([7], 2),
            ([5,7], 0),
            ([4,5,7], 4)
        ])
    def test_get_pivots_exception(self, list, number_of_pivots):
        with pytest.raises(Exception):
            algo = QuickSort()
            algo.get_pivots(list,number_of_pivots)

    @pytest.mark.parametrize("list, number_of_pivots, expected",
        [
            ([1,2,3], 1, [1]),
            ([1,2,3], 2, [1,2]),
            ([1,2,3], 3, [1,2,3])
        ])
    def test_get_pivots(self, list, number_of_pivots, expected):
        algo = QuickSort()
        obtained = algo.get_pivots(list,number_of_pivots)
        assert number_of_pivots == len(obtained)
        assert expected == obtained

    @pytest.mark.parametrize("list, number_of_pivots, expected",
        [
            ([1,2,3], 1, [3]),
            ([1,2,3], 2, [2,3]),
            ([1,2,3], 3, [1,2,3])
        ])
    def test_get_last_as_pivots(self, list, number_of_pivots, expected):
        algo = QuickSort()
        obtained = algo.get_last_as_pivots(list,number_of_pivots)
        assert expected == obtained
