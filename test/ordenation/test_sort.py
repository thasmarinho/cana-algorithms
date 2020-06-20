import pytest
from algorithms.ordenation import BubbleSort

testdata = [
    ([], []),
    ([7], [7]),
    ([1,2,3], [1,2,3]),
    ([3,5,1], [1,3,5]),
    ([191,2,73,1,7,3,5], [1,2,3,5,7,73,191]),
    (['C','B','D'], ['B','C','D']),
    ([-9,0,1,5,3,-1,4,2], [-9,-1,0,1,2,3,4,5])
]


@pytest.mark.parametrize("original, expected", testdata)
def test_bubble_sort(original, expected):
    algo = BubbleSort()
    obtained = algo.sort(original)

    assert expected == obtained
