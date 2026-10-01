class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        a = 0
        b = {}
        c = 0

        d = [i for i in range(1, (len(grid) ** 2) + 1)]

        for i in grid:
            for val in i:
                if val not in b:
                    b[val] = 1
                else:
                    b[val] += 1
                    c = val

        for key in d:
            if key not in b:
                a = key

        return [c, a]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna