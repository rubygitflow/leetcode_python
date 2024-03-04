# https://leetcode.com/problems/water-and-jug-problem/description/
# 365. Water and Jug Problem

# You are given two jugs with capacities jug1Capacity and jug2Capacity liters. There is an infinite amount of water supply available. Determine whether it is possible to measure exactly targetCapacity liters using these two jugs.
# If targetCapacity liters of water are measurable, you must have targetCapacity liters of water contained within one or both buckets by the end.

# Operations allowed:
# Fill any of the jugs with water.
# Empty any of the jugs.
# Pour water from one jug into another till the other jug is completely full, or the first jug itself is empty.

# Example 1:
# Input: jug1Capacity = 3, jug2Capacity = 5, targetCapacity = 4
# Output: true
# Explanation: The famous Die Hard example 

# Example 2:
# Input: jug1Capacity = 2, jug2Capacity = 6, targetCapacity = 5
# Output: false

# Example 3:
# Input: jug1Capacity = 1, jug2Capacity = 2, targetCapacity = 3
# Output: true
 

# Constraints:
# 1 <= jug1Capacity, jug2Capacity, targetCapacity <= 106

def canMeasureWater(
    jug1Capacity: int, jug2Capacity: int, targetCapacity: int
) -> bool:
    definition = jug1Capacity - jug2Capacity
    summ = jug1Capacity + jug2Capacity
    return (
        targetCapacity % jug1Capacity == 0 or
        targetCapacity % jug2Capacity == 0 or
        targetCapacity % definition == 0 or
        targetCapacity % summ == 0 or
        targetCapacity % jug1Capacity % definition == 0 or
        targetCapacity % jug2Capacity % definition == 0 or
        targetCapacity % summ % definition == 0
    )

canMeasureWater(2,3,1)
# Output: True
canMeasureWater(4,5,11)
# Output: True
canMeasureWater(2,6,5)
# Output: False
