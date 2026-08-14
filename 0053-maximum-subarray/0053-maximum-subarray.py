class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=nums[0]
        sum=0
        for i in (nums):
            if sum<0:
                sum = 0
            sum+=i
            maxi=max(sum,maxi)
        return maxi