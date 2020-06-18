import pytest
from algorithms.ordenation import BubbleSort

def test_sort_empty_list():
    original = []
    expected = []

    algo = BubbleSort()
    obtained = algo.sort(original)

    assert obtained == expected

def test_sort_single_element_list():
    original = [7]
    expected = [7]

    algo = BubbleSort()
    obtained = algo.sort(original)

    assert obtained == expected

def test_sort_desc_list():
    original = [3,2,1]
    expected = [1,2,3]

    algo = BubbleSort()
    obtained = algo.sort(original)

    assert obtained == expected

def test_already_sorted_list():
    original = [1,2,3]
    expected = [1,2,3]

    algo = BubbleSort()
    obtained = algo.sort(original)

    assert obtained == expected

def test_unsorted_list():
    original = [191,2,73,1,7,3,5]
    expected = [1,2,3,5,7,73,191]

    algo = BubbleSort()
    obtained = algo.sort(original)

    assert obtained == expected

def test_not_int_list():
    original = ['C','B','D']
    expected = ['B','C','D']

    algo = BubbleSort()
    obtained = algo.sort(original)

    assert obtained == expected
