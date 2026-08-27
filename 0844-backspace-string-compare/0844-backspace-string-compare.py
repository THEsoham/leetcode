class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        s1 = []
        s2 = []

        for i in s:
            if len(s1) == 0:
                if i != '#':
                    s1.append(i)
            elif i == '#':
                s1.pop()
            else:
                s1.append(i)

        for j in t:
            if len(s2) == 0:
                if j != '#':
                    s2.append(j)
            elif j == '#':
                s2.pop()
            else:
                s2.append(j)


        if s1 == s2:
            return True
        else:
            return False

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna