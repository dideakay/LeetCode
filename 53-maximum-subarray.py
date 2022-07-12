class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largestSum = -sys.maxint - 1
        newSum = 0
        
        for i in range(0,len(nums)):

            if(newSum < 0):
                newSum=0
            newSum=nums[i] + newSum
            if(newSum >= largestSum):
                largestSum=newSum
            
        return largestSum
            
