# https://leetcode.com/problems/top-k-frequent-words/description/
# 692. Top K Frequent Words

# Given an array of strings words and an integer k, return the k most frequent strings.
# Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

# Example 1:
# Input: words = ["i","love","leetcode","i","love","coding"], k = 2
# Output: ["i","love"]
# Explanation: "i" and "love" are the two most frequent words.
# Note that "i" comes before "love" due to a lower alphabetical order.

# Example 2:
# Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
# Output: ["the","is","sunny","day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.

# Constraints:
# 1 <= words.length <= 500
# 1 <= words[i].length <= 10
# words[i] consists of lowercase English letters.
# k is in the range [1, The number of unique words[i]]

####################
# https://leetcode.com/problems/top-k-frequent-elements/description/
# 347. Top K Frequent Elements

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

# Constraints:
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.


from collections import Counter #, defaultdict
from typing import List

class Solution:
    def topKFrequentWords(self, words: List[str], k: int) -> List[str]:
        data = Counter(words)
        # сортировка по количествам (values) и отображение слов (keys)
        # в количестве k
        return sorted(data, key=lambda x: (-data[x], x))[:k]
    def topKFrequentElements(self, nums: List[int], k: int) -> List[int]:
        data = Counter(nums)
        # data = defaultdict(int)
        # for c in nums:
        #     data[c] += 1
        # сортировка по количествам (values) и отображение элементов (keys)
        # в количестве k
        return sorted(data, key=lambda x: (-data[x], x))[:k]

words = ["i","love","leetcode","i","love","coding"]
Solution().topKFrequentWords(words, 2)
# Output: ["i","love"]

words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
Solution().topKFrequentWords(words, 4)
# Output: ["the","is","sunny","day"]

# nums = [1,1,1,2,2,3]
# Output: [1,2]
nums = [10,11,13,25,22,30,42,10,]
# Output: [10, 11]
Solution().topKFrequentElements(nums, 2)
