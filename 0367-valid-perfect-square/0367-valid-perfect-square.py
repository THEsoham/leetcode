class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start = 1
        end = num
        def binarysearch(start, end):
            mid = (start + end)//2
            if start > end:
                return False
            if mid * mid == num:
                return True
            elif mid * mid > num:
                end = mid - 1
                return binarysearch(start, end)
            elif mid * mid < num:
                start = mid + 1
                return binarysearch(start, end)

        return binarysearch(1, num)
    