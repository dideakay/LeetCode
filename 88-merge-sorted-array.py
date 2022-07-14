class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1Copy = nums1.copy()
        i1 = 0
        i2 = 0
        for i in range(m+n):
            if(i1<=m-1 and i2<=n-1):
                if(nums1Copy[i1] <= nums2[i2]):
                    nums1[i] = nums1Copy[i1]
                    i1+=1
                else:
                    nums1[i] = nums2[i2]
                    i2+=1
            elif(i1<=m-1 and i2>n-1 ):
                nums1[i] = nums1Copy[i1]
                i1 += 1
            elif(i1>m-1 and i2<=n-1 ):
                nums1[i] = nums2[i2]
                i2+=1
        
