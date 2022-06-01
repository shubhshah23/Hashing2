class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 1, 2, 4, 7, 3, -2, -1, 1, 4, 2]
        #  1, 3, 7, 14, 17, 15, 14, 15, 19, 21
        # totalSum (7) - x = 7
        # totalSum - k?
        
        prevSum = {}
        currentSum = 0
        prevSum[0] = 1
        counter = 0
        for num in nums:
            currentSum += num 
            if ((currentSum-k) in prevSum):
                counter+= prevSum[currentSum-k]
            prevSum[currentSum] = prevSum.get(currentSum, 0) + 1
        return counter
