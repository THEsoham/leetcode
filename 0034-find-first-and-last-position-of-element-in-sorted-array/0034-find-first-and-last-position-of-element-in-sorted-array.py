class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(nums)-1
        lower_ans = -1
        upper_ans = -1

        while left <= right:
            mid_1 = (left + right) // 2

            if nums[mid_1] < target:
                left = mid_1 + 1
            elif nums[mid_1] > target:
                right = mid_1 - 1
            else:
                lower_ans = mid_1
                right = mid_1 - 1
                
        left = 0
        right = len(nums)-1

        while left <= right:
            mid_2 = (left + right) // 2

            if nums[mid_2] < target:
                left = mid_2 + 1
            elif nums[mid_2] > target:
                right = mid_2 - 1
            else:
                upper_ans = mid_2
                left = mid_2 +1


        return [lower_ans,upper_ans]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna