class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums1Dict = defaultdict(int)
        resultDict = defaultdict(int)
        result = []
        
        for i in range(len(nums1)):
            nums1Dict[nums1[i]] = nums1.count(nums1[i])
            
        for i in range(len(nums2)):
            if(nums1Dict[nums2[i]]):
                resultDict[nums2[i]] = min(nums1Dict[nums2[i]],  nums2.count(nums2[i]))
        
        for i in range(len(nums2)):
            if(resultDict[nums2[i]]):
                result.append(nums2[i])
                resultDict[nums2[i]]-=1
                
        return(result)
