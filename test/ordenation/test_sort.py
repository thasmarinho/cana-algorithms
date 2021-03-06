import pytest
from algorithms.ordenation import BubbleSort
from algorithms.ordenation import ShellSort
from algorithms.ordenation import MergeSort
from algorithms.ordenation import QuickSort
from algorithms.ordenation import HeapSort

testdata = [
    ([], []),
    ([7], [7]),
    ([7, 5], [5, 7]),
    ([1, 2, 3], [1, 2, 3]),
    ([3, 5, 1, 4], [1, 3, 4, 5]),
    ([3, 3, 3, 3], [3, 3, 3, 3]),
    ([191, 2, 73, 1, 7, 3, 5], [1, 2, 3, 5, 7, 73, 191]),
    (['C', 'B', 'D'], ['B', 'C', 'D']),
    ([-9, 0, 1, 5, 3, -1, 4, 2], [-9, -1, 0, 1, 2, 3, 4, 5]),
    ([-16, -3, -55], [-55, -16, -3])
]


@pytest.mark.parametrize("original, expected", testdata)
class TestSortClass:

    def test_bubble_sort(self, original, expected):
        algo = BubbleSort()
        obtained = algo.sort(original)

        assert expected == obtained

    def test_shell_sort(self, original, expected):
        algo = ShellSort()
        obtained = algo.sort(original)

        assert expected == obtained

    def test_merge_sort(self, original, expected):
        algo = MergeSort()
        obtained = algo.sort(original)

        assert expected == obtained

    def test_quick_sort(self, original, expected):
        algo = QuickSort()
        obtained = algo.sort(original)

        assert expected == obtained

    def test_quick_sort_with_two_pivots(self, original, expected):
        algo = QuickSort()
        obtained = algo.sort_with_two_pivots(original)

        assert expected == obtained

    def test_heap_sort(self, original, expected):
        algo = HeapSort()
        obtained = algo.sort(original)

        assert expected == obtained
