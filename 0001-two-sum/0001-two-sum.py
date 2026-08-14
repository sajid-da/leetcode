class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr =len(nums)
        for i in range(arr-1):
            for j in range(i+1,arr):
                if nums[i]+nums[j] == target:
                    return i,j
                j+=1
                
    