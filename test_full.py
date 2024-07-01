import pytest

from collect_all_apples_in_tree import Solution as Solution1443
from single_number import Solution as Solution136_137
from top_k_frequent_words import Solution as Solution347_692

def test_the_top_k_frequent_words():
    assert ["i","love"] == Solution347_692().topKFrequentWords(["i","love","leetcode","i","love","coding"], 2)
    assert ["the","is","sunny","day"] == Solution347_692().topKFrequentWords(["the","day","is","sunny","the","the","the","sunny","is","is"], 4)
    assert ["is", "the"] == Solution347_692().topKFrequentWords(["the","the","the","day","sunny","sunny","is","is","is"], 2)
    assert ["is", "the", "sunny", "day"] == Solution347_692().topKFrequentWords(["the","the","the","day","sunny","sunny","is","is","is"], 6)

def test_the_top_k_frequent_elements():
    assert [1,2] == Solution347_692().topKFrequentElements([1,1,1,2,2,3], 2)
    assert [1] == Solution347_692().topKFrequentElements([1], 1)
    assert [10, 11] == Solution347_692().topKFrequentElements([10,11,13,25,22,30,42,10], 2)
    assert [10, 11, 13] == Solution347_692().topKFrequentElements([10,11,13,25,22,30,42,10], 3)
    assert [10, 11, 13, 22, 25, 30, 42] == Solution347_692().topKFrequentElements([10,11,13,25,22,30,42,10], 0)
    assert [10, 11] == Solution347_692().topKFrequentElements([10,11,13,25,22,30,42,10], -2)
    assert [0, 1] == Solution347_692().topKFrequentElements([1,1,1,2,2,3,0,0,0,5,5,5], 2)
    assert [0, 1] == Solution347_692().topKFrequentElements([1,1,1,2,2,3,5,5,5,0,0,0], 2)

# Python-case only
# def test_the_single_number_bf():
#     assert 99 == Solution136_137().singleNumberBF([0,1,0,1,0,1,99])
#     assert 0 == Solution136_137().singleNumberBF([0,1,0,1,0,1])

# Python-case only
# def test_the_single_number_iii():
#     assert 1 == Solution136_137().singleNumberIII([2,2,1,1,1])
#     assert 1 == Solution136_137().singleNumberIII([2,2,1])
#     assert 4 == Solution136_137().singleNumberIII([4,1,2,1,2])
#     assert 1 == Solution136_137().singleNumberIII([1])

def test_the_single_number():
    assert 1 == Solution136_137().singleNumber([2,2,1,1,1])
    assert 1 == Solution136_137().singleNumber([2,2,1])
    assert 4 == Solution136_137().singleNumber([4,1,2,1,2])
    assert 1 == Solution136_137().singleNumber([1])

def test_the_single_number_ii():
    assert 3 == Solution136_137().singleNumberII([2,2,3,2])
    assert 99 == Solution136_137().singleNumberII([0,1,0,1,0,1,99])
    assert 0 == Solution136_137().singleNumberII([0,1,0,1,0,1])

def test_the_collect_all_apples_in_tree():
    assert Solution1443().minTime(7,[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]],[False,False,True,False,True,True,False]) == 8 
    assert Solution1443().minTime(7,[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]],[False,False,True,False,False,True,False]) == 6
    assert Solution1443().minTime(7,[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]],[False,False,False,False,False,False,False]) == 0
    assert Solution1443().minTime(7,[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]],[True,False,False,False,False,False,False]) == 0
    assert Solution1443().minTime(9,[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6],[4,7],[4,8]],[False,False,False,False,False,False,False,False,True]) == 6
    assert Solution1443().minTime(9,[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6],[4,7],[4,8]],[False,True,False,False,True,False,False,False,True]) == 6
