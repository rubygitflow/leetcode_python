# find a number from an array that adds up to a given number
# найти числа из массива дающих в сумме заданное число

from typing import List

def twoSum(nums: List[int], k: int) -> List[int]:
    ''' Complexity Time: O(logN) Memory: O(N) '''
    tmp = set()
    for i in nums:
        expected_number = k - i
        if expected_number in tmp:
            return [expected_number, i]
        else:
            tmp.add(i)
    return []

nums, K =[-1,2,5,8], 7
# Output: [2, 5]
nums, K =[2,4,5], 8
# Output: []

twoSum(nums, K)

def twoSumB(nums: List[int], k: int) -> List[int]:
    ''' Complexity Time: O(NlogN) Memory: O(1) '''
    length = len(nums)
    for i in range(length):
        expected_number = k - nums[i]
        l, r = i + 1, length - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == expected_number:
                return [expected_number, nums[i]]
            elif expected_number < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
    return []

nums, K =[-7,0,2,3,6,8,10,15,18,20], 10
# Output: [10, 0]
twoSumB(nums, K)

def twoSumTPA(nums: List[int], k: int) -> List[int]:
    ''' Two Pointers Approach: Complexity Time: O(N) Memory: O(1) '''
    length = len(nums)
    l, r = 0, length - 1
    while l < r:
        sum = nums[l] + nums[r]
        if sum == k:
            return [nums[l], nums[r]]
        elif sum < k:
            l += 1
        else:
            r -= 1
    return []

nums, K =[-9,-7,-2,-1,1,4,9,11], 3
# Output: [-1, 4]
twoSumTPA(nums, K)
