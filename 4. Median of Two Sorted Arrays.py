class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m1 = len(nums1)
        m2 = len(nums2)
        l = (m1 + m2)
        if l % 2 == 0:
            return (self.kth(nums1, nums2, l // 2) + self.kth(nums1, nums2, l // 2 - 1)) / 2

        else:
            return self.kth(nums1, nums2, l // 2)

    def kth(self, a, b, length):
        if not b:
            return a[length]
        if not a:
            return b[length]
        l1 = len(a)
        l2 = len(b)
        ia = l1 // 2
        ib = l2 // 2
        ma = a[ia]
        mb = b[ib]
        if ia + ib < length:
            if ma > mb:
                return self.kth(a, b[ib + 1:], length - ib - 1)
            else:
                return self.kth(a[ia + 1:], b, length - ia - 1)
        else:
            if ma > mb:
                return self.kth(a[:ia], b, length)
            else:
                return self.kth(a, b[:ib], length)
