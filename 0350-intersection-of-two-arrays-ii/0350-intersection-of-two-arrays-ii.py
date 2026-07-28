class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l2 = []
        if len(nums1) < len(nums2):
            smaller = nums1
            bigger = nums2
        else:
            smaller = nums2
            bigger = nums1
        
        for i in smaller:
            if i in bigger:
                l2.append(i)
                bigger.remove(i)
        return l2