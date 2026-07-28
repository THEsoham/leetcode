class Solution(object):
    def intersection(self, nums1, nums2):

        l1 = []

        if len(nums1) <= len(nums2):
            smaller_array = nums1
            bigger_array = nums2
        else:
            smaller_array = nums2
            bigger_array = nums1

        for i in smaller_array:
            if i in bigger_array and i not in l1:
                l1.append(i)

        return l1