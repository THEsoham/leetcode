class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        area = 0

        while left < right:

            w = right - left
            h = min(height[left], height[right])
            a = w * h

            if a > area:
                area = a

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return area

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna