class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        best_length = 0
        window = set()

        for right in range(len(s)):

            while s[right] in window:        # Q1: which character causes the problem?
                window.remove(s[left])      # Q2: which character leaves when left moves?
                left += 1

            window.add(s[right])             # Q3: which character joins the window now?

            best_length = max(best_length, right-left+1)   # Q4: keep the larger of best and current window length

        return best_length
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna