# https://habr.com/ru/companies/yandex/articles/449890/
# Задача F. Слияние $k$ сортированных списков
# ---
# Как осуществить слияние k сортированных списков (решение)
# https://ru.stackoverflow.com/questions/927630/%D0%9A%D0%B0%D0%BA-%D0%BE%D1%81%D1%83%D1%89%D0%B5%D1%81%D1%82%D0%B2%D0%B8%D1%82%D1%8C-%D1%81%D0%BB%D0%B8%D1%8F%D0%BD%D0%B8%D0%B5-k-%D1%81%D0%BE%D1%80%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D1%85-%D1%81%D0%BF%D0%B8%D1%81%D0%BA%D0%BE%D0%B2?ysclid=ltankz97u649243670

# Даны k отсортированных в порядке неубывания массивов натуральных чисел, каждое из которых не превосходит 100. Требуется построить результат их слияния: отсортированный в порядке неубывания массив, содержащий все элементы исходных k массивов.
# Длина каждого массива не превосходит 10 ⋅ k.
# Постарайтесь, чтобы решение работало за время k ⋅ log(k) ⋅ n, если считать, что входные массивы имеют длину n.

########################
# https://leetcode.com/problems/merge-k-sorted-lists/description/
# 23. Merge k Sorted Lists

# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.

# Example 1:
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6

# Example 2:
# Input: lists = []
# Output: []

# Example 3:
# Input: lists = [[]]
# Output: []

# Constraints:
# k == lists.length
# 0 <= k <= 104
# 0 <= lists[i].length <= 500
# -104 <= lists[i][j] <= 104
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 104.

import sys
import time
import tracemalloc
from heapq import heappop, heappush
from list_node import ListNode, add_linked_list
from typing import List, Optional
from collections import Counter

class Solution:
    __focus_pos = {}
    __focus_val = {}
    __inputs = {}
    def __read_int(self) -> int:
        return int(sys.stdin.readline())
    def __read_array(self) -> List[int]:
        return list(map(int, sys.stdin.readline().split()))
    def __trace_start(self) -> float:
        tracemalloc.start()
        return time.time()
    def __trace_stop(self, t: float):
        print()
        print(time.time()-t)
        current, peak = tracemalloc.get_traced_memory()
        print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
        tracemalloc.stop()
        print()
    def inputAndCombineSortedLists(self) -> List[int]:
        ''' Merging K sorted lists (New method) '''
        n = self.__read_int()
        inputs = {}
        for i in range(n):
            inputs[i] = self.__read_array()
        t = self.__trace_start()
        c = Counter()
        for i in range(n):
            c += Counter(inputs[i][1:])
        outputs = []
        for i in sorted(c.keys()):
            outputs += [i for _ in range(c[i])]
        self.__trace_stop(t)
        return outputs
    def __shift_inputs(self, arr_id: int, from_pos: int):
        len = self.__inputs[arr_id][0]
        if from_pos < len:
            self.__change_focus(arr_id, from_pos + 1)
        else:
            self.__focus_pos.pop(arr_id)
            self.__focus_val.pop(arr_id)
    def __change_focus(self, arr_id: int, pos: int):
        self.__focus_pos[arr_id] = pos
        self.__focus_val[arr_id] = self.__inputs[arr_id][pos]
    def __iterateSortedLists(self) -> List[int]:
        output = []
        k = 0
        while len(self.__focus_pos) > 0:
            k += 1
            arr_id = min(self.__focus_val, key=self.__focus_val.get)
            old_pos = self.__focus_pos[arr_id]
            output.append(self.__inputs[arr_id][old_pos])
            self.__shift_inputs(arr_id, old_pos)
            if k > 1000000:
                break
        return output
    def inputAndCombineSortedListsOld(self) -> List[int]:
        ''' Merging K sorted lists (Old method) '''
        n = self.__read_int()
        for i in range(n):
            self.__inputs[i] = self.__read_array()
        t = self.__trace_start()
        for i in range(n):
            if self.__inputs[i][0] > 0:
                self.__change_focus(i, 1)
        output = self.__iterateSortedLists()
        self.__trace_stop(t)
        return output
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ''' Merging K sorted lists (final)'''
        if not lists:
            return []

        head = ListNode(0)
        tail = head
        heap = [] # where the pop method returns the smallest item
        for i in range(len(lists)):
            if lists[i]:
                heappush(heap, (lists[i].val, i))
        while heap:
            list_index = heappop(heap)[1]
            tail.next = lists[list_index]
            lists[list_index] = lists[list_index].next
            if lists[list_index]:
                heappush(heap, (lists[list_index].val, list_index))
            tail = tail.next
        return head.next


# 3
# 3 1 44 88
# 3 5 16 78
# 3 23 44 98
# Output: 
# [1, 5, 16, 23, 44, 44, 78, 88, 98]

# 4
# 6 2 26 64 88 96 96
# 4 8 20 65 86
# 7 1 4 16 42 58 61 69
# 3 1 84 86
# Output: 
# [1, 1, 2, 4, 8, 16, 20, 26, 42, 58, 61, 64, 65, 69, 84, 86, 86, 88, 96, 96]

if __name__ == "__main__":
    print("Merge k Sorted Lists (Algorithm I)")
    print("Enter the number of arrays and the arrays themselves:")
    print(Solution().inputAndCombineSortedLists())
    # 0.0005667209625244141
    # Current memory usage is 0.002923MB; Peak was 0.003371MB

    print("Merge k Sorted Lists (Algorithm II)")
    print("Enter the number of arrays and the arrays themselves:")
    print(Solution().inputAndCombineSortedListsOld())
    # 0.0002269744873046875
    # Current memory usage is 0.000512MB; Peak was 0.000896MB

    print("Merge k Sorted Lists (final")
    print(Solution().mergeKLists([add_linked_list([2,6]),add_linked_list([1,4,5]),add_linked_list([1,3,4])]))
    # Output: [1,1,2,3,4,4,5,6]
