class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summ = 0
        maxi = nums[0]
        for i in nums :
            if summ < 0:
                summ = 0
            summ+=i
            maxi=max(summ,maxi)
        return maxi