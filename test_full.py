# https://docs.pytest.org/en/latest/
# https://pypi.org/project/pytest-assertcount/

import pytest

from list_node import ListNode, add_linked_list

from collect_all_apples_in_tree import Solution as Solution1443
from single_number import Solution as Solution136_137
from top_k_frequent_words import Solution as Solution347_692
from delete_characters_to_make_fancy_string import Solution as Solution1957
from count_number_of_special_subsequences import Solution as Solution1955
from check_if_move_is_legal import Solution as Solution1958
from minimum_time_for_k_virus_variants_to_spread import Solution as Solution1956
from minimum_time_to_type_word_using_special_typewriter import Solution as Solution1974
from maximum_matrix_sum import Solution as Solution1975
from merging_k_sorted_lists import Solution as Solution23
from advantage_shuffle import Solution as Solution870
from alternating_digit_sum import Solution as Solution258_2544
from best_time_to_buy_and_sell_stock import Solution as Solution121_122_123_188_309_714


def test_the_best_time_to_buy_and_sell_stock():
    assert Solution121_122_123_188_309_714().maxProfit([7,1,5,3,6,4]) == 5
    assert Solution121_122_123_188_309_714().maxProfit([7,6,4,3,1]) == 0

def test_the_best_time_to_buy_and_sell_stock_ii():
    assert Solution121_122_123_188_309_714().maxProfitII([7,1,5,3,6,4]) == 7
    assert Solution121_122_123_188_309_714().maxProfitII([1,2,3,4,5]) == 4
    assert Solution121_122_123_188_309_714().maxProfitII([7,6,4,3,1]) == 0
    assert Solution121_122_123_188_309_714().maxProfitII([7]) == 0
    assert Solution121_122_123_188_309_714().maxProfitII([]) == 0

def test_the_best_time_to_buy_and_sell_stock_iii():
    assert Solution121_122_123_188_309_714().maxProfitIII([3,3,5,0,0,3,1,4]) == 6
    assert Solution121_122_123_188_309_714().maxProfitIII([1,2,3,4,5]) == 4
    assert Solution121_122_123_188_309_714().maxProfitIII([7,6,4,3,1]) == 0
    assert Solution121_122_123_188_309_714().maxProfitIII([7]) == 0
    assert Solution121_122_123_188_309_714().maxProfitIII([]) == 0

def test_the_best_time_to_buy_and_sell_stock_iv():
    assert Solution121_122_123_188_309_714().maxProfitIV(2, [2,4,1]) == 2
    assert Solution121_122_123_188_309_714().maxProfitIV(2, [3,2,6,7,5,0,3]) == 8
    assert Solution121_122_123_188_309_714().maxProfitIV(2, [3,2,6,5,0,3]) == 7

def test_the_best_time_to_buy_and_sell_stock_with_cooldown():
    assert Solution121_122_123_188_309_714().maxProfitWithHold([1,2,3,0,2]) == 3
    assert Solution121_122_123_188_309_714().maxProfitWithHold([1]) == 0

def test_the_best_time_to_buy_and_sell_stock_with_fee_ex():
    assert Solution121_122_123_188_309_714().maxProfitAfterFeeEx([1,3,2,8,4,9], 2) == 8
    assert Solution121_122_123_188_309_714().maxProfitAfterFeeEx([1,3,7,5,10,3], 3) == 6
    assert Solution121_122_123_188_309_714().maxProfitAfterFeeEx([8,9,7,6,8,8], 2) == 0

@pytest.mark.skip(reason="Python-case only")
def test_the_best_time_to_buy_and_sell_stock_with_fee():
    assert Solution121_122_123_188_309_714().maxProfitAfterFee([1,3,2,8,4,9], 2) == 8
    assert Solution121_122_123_188_309_714().maxProfitAfterFee([1,3,7,5,10,3], 3) == 6
    assert Solution121_122_123_188_309_714().maxProfitAfterFee([8,9,7,6,8,8], 2) == 0


def test_the_add_digits():
    assert Solution258_2544().addDigits(38) == 2
    assert Solution258_2544().addDigits(0) == 0
    assert Solution258_2544().addDigits(886995) == 9
    assert Solution258_2544().addDigits(1) == 1

def test_the_alternating_digit_sum():
    assert Solution258_2544().alternateDigitSum(521) == 4
    assert Solution258_2544().alternateDigitSum(111) == 1
    assert Solution258_2544().alternateDigitSum(886996) == 0
    assert Solution258_2544().alternateDigitSum(885996) == -1
    assert Solution258_2544().alternateDigitSum(886995) == 1


def test_the_advantage_shuffle():
    assert Solution870().advantageCount([2,7,11,15], [1,10,4,11]) == [2,11,7,15]
    assert Solution870().advantageCount([12,24,8,32], [13,25,32,11]) == [24,32,8,12]
    assert Solution870().advantageCount([12,24,8], [13,25,32,11]) == []


@pytest.mark.skip(reason="Python-task only")
def test_the_merging_k_sorted_lists():
    assert str(Solution23().mergeKLists([add_linked_list([2,6]),add_linked_list([1,4,5]),add_linked_list([1,3,4])])) == '[1,1,2,3,4,4,5,6]'


def test_the_maximum_matrix_sum():
    assert Solution1975().maxMatrixSum([[1,-1],[-1,1]]) == 4
    assert Solution1975().maxMatrixSum([[1,2,3],[-1,-2,-3],[1,2,3]]) == 16


def test_the_minimum_time_to_type_word_using_special_typewriter():
    assert Solution1974().minTimeToType("abc") == 5
    assert Solution1974().minTimeToType("bza") == 7
    assert Solution1974().minTimeToType("zjpc") == 34


@pytest.mark.skip(reason="Python-case only")
def test_the_minimum_time_for_k_virus_variants_to_spread():
    assert Solution1956().minDayskVariants([[1,1],[6,1]], 2) == 3
    assert Solution1956().minDayskVariants([[3,3],[1,2],[9,2]], 2) == 2
    assert Solution1956().minDayskVariants([[3,3],[1,2],[9,2]], 3) == 4


def test_the_check_if_move_is_legal():
    board, rMove, cMove, color = [[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],["W","B","B",".","W","W","W","B"],[".",".",".","B",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."]], 4, 3, "B"
    assert Solution1958().checkMove(board, rMove, cMove, color) == True
    board, rMove, cMove, color = [[".",".",".",".",".",".",".","."],[".","B",".",".","W",".",".","."],[".",".","W",".",".",".",".","."],[".",".",".","W","B",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".","B","W",".","."],[".",".",".",".",".",".","W","."],[".",".",".",".",".",".",".","B"]], 4, 4, "W"
    assert Solution1958().checkMove(board, rMove, cMove, color) == False


@pytest.mark.skip(reason="Python-case only")
def test_the_count_number_of_special_subsequences_forloop():
    assert Solution1955().countSpecialSubsequences([0,1,2]) == 1
    assert Solution1955().countSpecialSubsequences([0,1,2,0]) == 1
    assert Solution1955().countSpecialSubsequences([0,1,2,2]) == 3
    assert Solution1955().countSpecialSubsequences([2,2,0,0]) == 0
    assert Solution1955().countSpecialSubsequences([0,1,2,0,1,2]) == 7

def test_the_count_number_of_special_subsequences_reduce():
    assert Solution1955().countSpecialSubsequencesII([0,1,2]) == 1
    assert Solution1955().countSpecialSubsequencesII([0,1,2,0]) == 1
    assert Solution1955().countSpecialSubsequencesII([0,1,2,2]) == 3
    assert Solution1955().countSpecialSubsequencesII([2,2,0,0]) == 0
    assert Solution1955().countSpecialSubsequencesII([0,1,2,0,1,2]) == 7


def test_the_delete_characters_to_make_fancy_string_forloop():
    assert Solution1957().makeFancyString("leeetcode") == "leetcode"
    assert Solution1957().makeFancyString("aaabaaaa") == "aabaa"
    assert Solution1957().makeFancyString("aab") == "aab"

def test_the_delete_characters_to_make_fancy_string_reduce():
    assert Solution1957().makeFancyStringII("leeetcode") == "leetcode"
    assert Solution1957().makeFancyStringII("aaabaaaa") == "aabaa"
    assert Solution1957().makeFancyStringII("aab") == "aab"


def test_the_top_k_frequent_words():
    assert Solution347_692().topKFrequentWords(["i","love","leetcode","i","love","coding"], 2) == ["i","love"]
    assert Solution347_692().topKFrequentWords(["the","day","is","sunny","the","the","the","sunny","is","is"], 4) == ["the","is","sunny","day"]
    assert Solution347_692().topKFrequentWords(["the","the","the","day","sunny","sunny","is","is","is"], 2) == ["is", "the"]
    assert Solution347_692().topKFrequentWords(["the","the","the","day","sunny","sunny","is","is","is"], 6) == ["is", "the", "sunny", "day"]

def test_the_top_k_frequent_elements():
    assert Solution347_692().topKFrequentElements([1,1,1,2,2,3], 2) == [1,2]
    assert Solution347_692().topKFrequentElements([1], 1) == [1]
    assert Solution347_692().topKFrequentElements([10,11,13,25,22,30,42,10], 2) == [10, 11]
    assert Solution347_692().topKFrequentElements([10,11,13,25,22,30,42,10], 3) == [10, 11, 13]
    assert Solution347_692().topKFrequentElements([10,11,13,25,22,30,42,10], 0) == [10, 11, 13, 22, 25, 30, 42]
    assert Solution347_692().topKFrequentElements([10,11,13,25,22,30,42,10], -2) == [10, 11]
    assert Solution347_692().topKFrequentElements([1,1,1,2,2,3,0,0,0,5,5,5], 2) == [0, 1]
    assert Solution347_692().topKFrequentElements([1,1,1,2,2,3,5,5,5,0,0,0], 2) == [0, 1]


@pytest.mark.skip(reason="Python-case only")
def test_the_single_number_bf():
    assert Solution136_137().singleNumberBF([0,1,0,1,0,1,99]) == 99
    assert Solution136_137().singleNumberBF([0,1,0,1,0,1]) == 0

def test_the_single_number_reduce():
    assert Solution136_137().singleNumberIII([2,2,1,1,1]) == 1
    assert Solution136_137().singleNumberIII([2,2,1]) == 1
    assert Solution136_137().singleNumberIII([4,1,2,1,2]) == 4
    assert Solution136_137().singleNumberIII([1]) == 1

@pytest.mark.skip(reason="Python-case only")
def test_the_single_number_forloop():
    assert Solution136_137().singleNumber([2,2,1,1,1]) == 1
    assert Solution136_137().singleNumber([2,2,1]) == 1
    assert Solution136_137().singleNumber([4,1,2,1,2]) == 4
    assert Solution136_137().singleNumber([1]) == 1

def test_the_single_number_ii():
    assert Solution136_137().singleNumberII([2,2,3,2]) == 3
    assert Solution136_137().singleNumberII([0,1,0,1,0,1,99]) == 99
    assert Solution136_137().singleNumberII([0,1,0,1,0,1]) == 0


def test_the_collect_all_apples_in_tree():
    assert Solution1443().minTime(7,[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]],[False,False,True,False,True,True,False]) == 8 
    assert Solution1443().minTime(7,[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]],[False,False,True,False,False,True,False]) == 6
    assert Solution1443().minTime(7,[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]],[False,False,False,False,False,False,False]) == 0
    assert Solution1443().minTime(7,[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]],[True,False,False,False,False,False,False]) == 0
    assert Solution1443().minTime(9,[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6],[4,7],[4,8]],[False,False,False,False,False,False,False,False,True]) == 6
    assert Solution1443().minTime(9,[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6],[4,7],[4,8]],[False,True,False,False,True,False,False,False,True]) == 6
