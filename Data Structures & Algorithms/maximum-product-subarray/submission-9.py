'''
Find a subarray with the largest product

A subarray is the contiguous non-empty sequence

Brute force
1. Try each subarray

How would we speed this up?
    We can use dynamic programming to store products of subarrays


[2,3,-2,4]

Problem: The largest subarray doesn't mean that the next subarray will use that product. A negative would make it positive

I suppose we want the largest and smallest. We can choose which to use 

[2,3,-2,4]

Largest/smallest product starting at i
Largest: [6, 3, -2, 4]
Smallest: [-48, -24, -8, 4]


[-3, -1, -1]
Largest: [-1, ]
Smallest: [-1, ]


'''


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest = []
        smallest = []

        for idx in range(len(nums) - 1, -1, -1):
            n = nums[idx]
            p_largest =  (largest[-1] if len(largest) else 1) * n
            p_smallest = (smallest[-1] if len(smallest) else 1) * n
        
            largest.append(max(p_largest, p_smallest, n))
            smallest.append(min(p_largest, p_smallest, n))

        return max(largest)