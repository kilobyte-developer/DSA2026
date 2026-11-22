class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mp = {}

        for i in nums:
            mp[i] = True

        for j in range(len(nums)+1):
            if j not in mp:
                return j 