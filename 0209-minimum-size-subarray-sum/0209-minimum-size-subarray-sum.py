class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        best = float('inf')
        sum_ = 0

        for right in range(len(nums)):         
            sum_ = sum_ + nums[right]
            while sum_ >= target:
                best = min(best, right - left + 1)   
                sum_ = sum_ - nums[left]
                left += 1                        

        if best == float('inf'):
            return 0
        else:
            return best

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna