class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        pivot = 0

        while pivot < len(nums):
            left = sum(nums[: pivot]) - pivot
            right = sum(nums[pivot+1:]) - pivot
            if  left  == right:
                return pivot
            pivot += 1
        
        return -1
