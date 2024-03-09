# Output all the unique pairs from a numeric array
# вывести все уникальные пары  из числового массива

from math import factorial
from typing import List

def fetchUniquePairs(nums: List[int]) -> List[List[int]]:
    ''' Output all the unique pairs from a numeric array '''
    if len(nums) < 2:
        return []
    nums = sorted(nums)
    double_i = set()
    output = []
    for i in range(len(nums) - 1):
        if nums[i] not in double_i:
            double_i.add(nums[i])
            double_j = set()
            for j in range(i + 1, len(nums)):
                if nums[j] not in double_j:
                    double_j.add(nums[j])
                    output.append([nums[i], nums[j]])
    return output

f = [0,0,0,1,1,2,4]
f = [0,1,1,0,0,2,4]
f = [4,0,1,0,1,2,0]
# Output: [[0, 0], [0, 1], [0, 2], [0, 4], [1, 1], [1, 2], [1, 4], [2, 4]]
fetchUniquePairs(f)

def countUniquePairs(nums: List[int]) -> List[List[int]]:
    ''' Just count all the unique pairs from the numeric array '''
    if len(nums) < 2:
        return 0
    unic = set(nums)
    # count duplicates
    setter, double = set(), set()
    for v in nums:
        if v in setter:
            double.add(v)
        setter.add(v)
    return (factorial(len(unic) - 1) if len(unic) > 1 else 0) + len(double)

f = [0,0,0,1,1,2,4]
f = [0,1,1,0,0,2,4]
f = [4,0,1,0,1,2,0]
# Output: 8
f = [0,0,0]
# Output: 1
f = [0,0,0,1]
# Output: 2
f = [0,1]
# Output: 2
countUniquePairs(f)
