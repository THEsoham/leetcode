class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        j = 0
        for i in range(m, len(nums1)):
            nums1[i] = nums2[j]
            j += 1
        
        for m in range(0, len(nums1)):
            for n in range(m+1, len(nums1)):
                if nums1[m] > nums1[n]:
                    nums1[m],nums1[n] = nums1[n],nums1[m]
        return nums1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna