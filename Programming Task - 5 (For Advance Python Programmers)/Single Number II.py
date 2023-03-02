"""
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,3,2]
Output: 3
Example 2:

Input: nums = [0,1,0,1,0,1,99]
Output: 99
 

Constraints:

1 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
Each element in nums appears exactly three times except for one element which appears once.
"""

class Solution:
	def singleNumber(self, nums: List[int]) -> int:

		# Let the numbers be x,y,z,.....
		# require sum should be 3x+3y+3z
		# original sum = 3x+3y+z
		# Subtract require sum from original sum
		# (3x+3y+3z) - (3x+3y-z) = 2z
		# div the ans by 2 = 2z/2 = z--> our ans

		return (3 * sum(set(nums)) - sum(nums)) // 2
