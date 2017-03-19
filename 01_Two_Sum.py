'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}
        for index,value in enumerate(nums):
            hash_map[value]=index
            print hash_map
        for index_1,value in enumerate(nums):
            if target-value in hash_map:
                index_2=hash_map[target-value]
                if index_1 != index_2:
                    return [index_1, index_2] # If you want index starts at 1, use return [index_1 + 1, index_2 + 1]
