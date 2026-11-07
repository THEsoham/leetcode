class Solution(object):
    def minSubArrayLen(self, target, nums):
        left = 0
        total = 0
        best = float('inf')

        for right in range(len(nums)):
            total += nums[right]

            while total >= target:
                best = min(best, right - left + 1)
                total -= nums[left]
                left += 1

        return 0 if best == float('inf') else best

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna