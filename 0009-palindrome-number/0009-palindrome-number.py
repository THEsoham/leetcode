class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            l1 = []
            for i in str(x):
                l1.append(i)
            if l1 == l1[::-1]:
                return True
            else:
                 return False
        