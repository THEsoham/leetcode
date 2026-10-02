class Solution(object):
    def majorityElement(self, nums):
        d = {}

        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        for key, value in d.items():
            if value > len(nums) / 2:
                return key

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna