class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        


        nums.sort()
        h1 = nums[-1]
        h2 = nums[-2]
        return ((h1-1)*(h2-1))