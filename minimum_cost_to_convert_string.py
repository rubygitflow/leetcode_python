# https://leetcode.com/problems/minimum-cost-to-convert-string-i/description/
# 2976. Minimum Cost to Convert String I

# You are given two 0-indexed strings source and target, both of length n and consisting of lowercase English letters. You are also given two 0-indexed character arrays original and changed, and an integer array cost, where cost[i] represents the cost of changing the character original[i] to the character changed[i].
# You start with the string source. In one operation, you can pick a character x from the string and change it to the character y at a cost of z if there exists any index j such that cost[j] == z, original[j] == x, and changed[j] == y.
# Return the minimum cost to convert the string source to the string target using any number of operations. If it is impossible to convert source to target, return -1.
# Note that there may exist indices i, j such that original[j] == original[i] and changed[j] == changed[i].

# Example 1:
# Input: source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20]
# Output: 28
# Explanation: To convert the string "abcd" to string "acbe":
# - Change value at index 1 from 'b' to 'c' at a cost of 5.
# - Change value at index 2 from 'c' to 'e' at a cost of 1.
# - Change value at index 2 from 'e' to 'b' at a cost of 2.
# - Change value at index 3 from 'd' to 'e' at a cost of 20.
# The total cost incurred is 5 + 1 + 2 + 20 = 28.
# It can be shown that this is the minimum possible cost.

# Example 2:
# Input: source = "aaaa", target = "bbbb", original = ["a","c"], changed = ["c","b"], cost = [1,2]
# Output: 12
# Explanation: To change the character 'a' to 'b' change the character 'a' to 'c' at a cost of 1, followed by changing the character 'c' to 'b' at a cost of 2, for a total cost of 1 + 2 = 3. To change all occurrences of 'a' to 'b', a total cost of 3 * 4 = 12 is incurred.

# Example 3:
# Input: source = "abcd", target = "abce", original = ["a"], changed = ["e"], cost = [10000]
# Output: -1
# Explanation: It is impossible to convert source to target because the value at index 3 cannot be changed from 'd' to 'e'.

# Constraints:
# 1 <= source.length == target.length <= 105
# source, target consist of lowercase English letters.
# 1 <= cost.length == original.length == changed.length <= 2000
# original[i], changed[i] are lowercase English letters.
# 1 <= cost[i] <= 106
# original[i] != changed[i]


#######################
# https://leetcode.com/problems/minimum-cost-to-convert-string-ii/description/
# 2977. Minimum Cost to Convert String II

# You are given two 0-indexed strings source and target, both of length n and consisting of lowercase English characters. You are also given two 0-indexed string arrays original and changed, and an integer array cost, where cost[i] represents the cost of converting the string original[i] to the string changed[i].
# You start with the string source. In one operation, you can pick a substring x from the string, and change it to y at a cost of z if there exists any index j such that cost[j] == z, original[j] == x, and changed[j] == y. You are allowed to do any number of operations, but any pair of operations must satisfy either of these two conditions:
# The substrings picked in the operations are source[a..b] and source[c..d] with either b < c or d < a. In other words, the indices picked in both operations are disjoint.
# The substrings picked in the operations are source[a..b] and source[c..d] with a == c and b == d. In other words, the indices picked in both operations are identical.
# Return the minimum cost to convert the string source to the string target using any number of operations. If it is impossible to convert source to target, return -1.
# Note that there may exist indices i, j such that original[j] == original[i] and changed[j] == changed[i].

# Example 1:
# Input: source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20]
# Output: 28
# Explanation: To convert "abcd" to "acbe", do the following operations:
# - Change substring source[1..1] from "b" to "c" at a cost of 5.
# - Change substring source[2..2] from "c" to "e" at a cost of 1.
# - Change substring source[2..2] from "e" to "b" at a cost of 2.
# - Change substring source[3..3] from "d" to "e" at a cost of 20.
# The total cost incurred is 5 + 1 + 2 + 20 = 28.
# It can be shown that this is the minimum possible cost.

# Example 2:
# Input: source = "abcdefgh", target = "acdeeghh", original = ["bcd","fgh","thh"], changed = ["cde","thh","ghh"], cost = [1,3,5]
# Output: 9
# Explanation: To convert "abcdefgh" to "acdeeghh", do the following operations:
# - Change substring source[1..3] from "bcd" to "cde" at a cost of 1.
# - Change substring source[5..7] from "fgh" to "thh" at a cost of 3. We can do this operation because indices [5,7] are disjoint with indices picked in the first operation.
# - Change substring source[5..7] from "thh" to "ghh" at a cost of 5. We can do this operation because indices [5,7] are disjoint with indices picked in the first operation, and identical with indices picked in the second operation.
# The total cost incurred is 1 + 3 + 5 = 9.
# It can be shown that this is the minimum possible cost.

# Example 3:
# Input: source = "abcdefgh", target = "addddddd", original = ["bcd","defgh"], changed = ["ddd","ddddd"], cost = [100,1578]
# Output: -1
# Explanation: It is impossible to convert "abcdefgh" to "addddddd".
# If you select substring source[1..3] as the first operation to change "abcdefgh" to "adddefgh", you cannot select substring source[3..7] as the second operation because it has a common index, 3, with the first operation.
# If you select substring source[3..7] as the first operation to change "abcdefgh" to "abcddddd", you cannot select substring source[1..3] as the second operation because it has a common index, 3, with the first operation.

# Constraints:
# 1 <= source.length == target.length <= 1000
# source, target consist only of lowercase English characters.
# 1 <= cost.length == original.length == changed.length <= 100
# 1 <= original[i].length == changed[i].length <= source.length
# original[i], changed[i] consist only of lowercase English characters.
# original[i] != changed[i]
# 1 <= cost[i] <= 106


from collections import defaultdict
from typing import List, Set, Dict

class Solution:
    def __compare_all_paths(self, original: List[str], changed: List[str], cost: List[int], original_set: Set[str], changed_set: Set[str]) -> Dict:
        graph = defaultdict(lambda: defaultdict(int))
        # fix initial costs
        # Step 2: Populate substring distances matrix
        for ori, cha, cos in zip(original, changed, cost):
            graph[ori][cha] = max(graph[ori][cha], cos)
        # bypass all connections
        # Step 3: Floyd-Warshall algorithm to calculate minimum distances between substrings
        for k in original_set.union(changed_set):   # intermediate bundle
            for i in original_set:                  # original bundle
                for j in changed_set:               # changed bundle
                    graph[i][j] = min(
                        (graph[i][j] or float('inf')),
                        (graph[i][k] or float('inf')) + (graph[k][j] or float('inf'))
                    )
        return graph

    def minimumCostI(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        '''
        Minimum Cost to Convert String I
        Time complexity: O(n) + /O( set(original) * set(changed) * (set(original)+set(changed))) ≈ const/ 
        Space complexity: O(1)
        '''
        # Step 1: Initialize necessary data structures and variables
        original_set = set(original)
        changed_set  = set(changed)
        # remove unchanged items
        actioned_inp = [v for v, w in zip(list(source), list(target)) if v != w]
        actioned_out = [w for v, w in zip(list(source), list(target)) if v != w]

        # Step PE:  proactive exit
        if any(set(actioned_inp) - original_set):
            return -1
        if any(set(actioned_out) - changed_set):
            return -1

        min_paths = self.__compare_all_paths(original, changed, cost, original_set, changed_set)

        res = 0
        # calculate labor costs
        # Step 4: "Dynamic programming" to find minimum cost
        for inp, out in zip(actioned_inp, actioned_out):
            res += min_paths[inp][out]
        return res if res < float('inf') else -1

    def minimumCostII(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        '''
        Minimum Cost to Convert String II
        '''
        # Step 1: Initialize necessary data structures and variables
        original_set = set(original)
        changed_set  = set(changed)
        source_len = len(source)
        dp = [float('inf')] * (source_len + 1)

        min_paths = self.__compare_all_paths(original, changed, cost, original_set, changed_set)

        # calculate labor costs
        # Step 4: "Dynamic programming" to find minimum cost
        dp[0] = 0;
        for i in range(source_len):
            if dp[i] == float('inf'):
                continue
            source_char = source[i]
            target_char = target[i]
            if source_char == target_char:
                dp[i + 1] = min(dp[i + 1], dp[i])
            for substring in original_set:
                substring_len = len(substring)
                if i + substring_len > source_len:
                    continue
                sub_source = source[i:i+substring_len]
                sub_target = target[i:i+substring_len]
                if not sub_source in original_set or not sub_target in changed_set:
                    continue
                if min_paths[sub_source][sub_target] != float('inf'):
                    dp[i + substring_len] = min(
                      dp[i + substring_len],
                      dp[i] + min_paths[sub_source][sub_target]
                    )
        return dp[source_len] if dp[source_len] < float('inf') else -1


print("Minimum Cost to Convert String I")

print(Solution().minimumCostI("abcd","acbe",["a","b","c","c","e","d"],["b","c","b","e","b","e"],[2,5,5,1,2,20]))
# Output: 28 (5 > 1+2)
print(Solution().minimumCostI("abcd","acbe",["a","b","c","c","f","e","d"],["b","c","b","f","e","b","e"],[2,5,5,1,2,1,20]));
# Output: 29 (5 > 1+2+1)
print(Solution().minimumCostI("aaaa","bbbb",["a","c"],["c","b"],[1,2]))
# Output: 12
print(Solution().minimumCostI("aaaa","bbbb",["a","c"],["d","b"],[1,2]))
# Output: -1
print(Solution().minimumCostI("aaaa","bbbb",["a","c","a","d","e"],["c","b","d","e","b"],[3,2,1,1,1]))
# Output: 12
print(Solution().minimumCostI("abcd","abce",["a"],["e"],[10000]))
# Output: -1
print(Solution().minimumCostI("aaa","aaa",["a"],["e"],[10000]))
# Output: 0


print("Minimum Cost to Convert String II")

print(Solution().minimumCostII("abcd","acbe",["a","b","c","c","e","d"],["b","c","b","e","b","e"],[2,5,5,1,2,20]))
# Output: 28
print(Solution().minimumCostII("fgh","ghh",["bcd","fgh","thh"],["cde","thh","ghh"],[1,3,5]))
# Output: 8
print(Solution().minimumCostII("fgh","ghh",["fgh","f","g","thh"],["thh","g","h","ghh"],[3,1,1,5]))
# Output: 2 (1+1 < 3+5)
print(Solution().minimumCostII("fgh","f&&",["fgh","fgh"],["f&&","f&"],[11,1]))
# Output: 11
print(Solution().minimumCostII("abcdefgh","acdeeghh",["bcd","fgh","thh"],["cde","thh","ghh"],[1,3,5]))
# Output: 9
print(Solution().minimumCostII("abcdefgh","addddddd",["bcd","defgh"],["ddd","ddddd"],[100,1578]))
# Output: -1
print(Solution().minimumCostII("aaa","aaa",["a"],["e"],[10000]))
# Output: 0
