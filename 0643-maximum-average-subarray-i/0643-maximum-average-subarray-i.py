class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        p1 = 0
        p2 = k
        tempSum = sum(nums[0:k])
        maxAvg = tempSum/float(k)
        while p2<len(nums):
            tempSum += nums[p2]
            tempSum -= nums[p1]
            tempAvg = tempSum/float(k)

            if tempAvg>maxAvg:
                maxAvg = tempAvg
            
            p2+=1
            p1+=1

        return maxAvg