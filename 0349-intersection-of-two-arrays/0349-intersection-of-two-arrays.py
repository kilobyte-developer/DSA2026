class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        mp = {}
        n = len(nums2)
        result = []
        for i in nums1:
            mp[i] = mp.get(i,0)+1
        
        for j in range(n):
            if nums2[j] in mp:
                if nums2[j] not in result:
                    result.append(nums2[j])

        return result