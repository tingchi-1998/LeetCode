#
# @lc app=leetcode id=27 lang=python
#
# [27] Remove Element
#

# @lc code=start
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0 #pointer
        for x in nums: #x represents the values in the array
            if x != val:
                nums[i] = x
                i += 1
        return i
        
# @lc code=end

