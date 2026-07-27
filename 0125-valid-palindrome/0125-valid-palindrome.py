class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s1 = ''.join([char for char in s if char.isalnum()])
        if s1.lower() == s1.lower()[::-1]:
            return True
        else:
            return False