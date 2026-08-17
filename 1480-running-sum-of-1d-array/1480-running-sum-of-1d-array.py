class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l1 = []
        sum_ = 0
        for i in range (len(nums)):
            sum_ = sum_ + nums[i] 
            l1.append(sum_)
        return (l1)