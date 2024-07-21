#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for x in range(len(nums)):
            for y in range(x+1,len(nums)):
                if(nums[x] + nums[y] == target):
                    return [x,y]

        
# @lc code=end

