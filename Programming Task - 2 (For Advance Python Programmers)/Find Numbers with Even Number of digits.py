"""
Given an array nums of integers, return how many of them contain an even number of digits.

 

Example 1:

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.
Example 2:

Input: nums = [555,901,482,1771]
Output: 1 
Explanation: 
Only 1771 contains an even number of digits.
 

Constraints:

1 <= nums.length <= 500
1 <= nums[i] <= 105
"""

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
	    # We are going to take advantage of the fact that the array only contains positive integers.
		# A common formula for finding the number of digits in a positive number is digits = floor(log10(num)) + 1
		# Even if the array contained negatives, you could just do the same with the absolute value of num.
		# This turns the runtime into O(N) and there is no additional space needed so O(1) space.
		# You also don't need to convert this into a string which a lot of other solutions do and has other implications in terms of space complexity.
        result = 0
        
        for num in nums:
            num_digits = floor(log10(num)) + 1
            if num_digits % 2 == 0:
                result += 1
                
        return result
