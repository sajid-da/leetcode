class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l=0
        maxi=sum(nums[:k])
        window_sum=maxi
        for right in range (k,len(nums)):
            window_sum += nums[right]
            window_sum -= nums[l]
            l+=1
            maxi = max(maxi,window_sum)
        return maxi/k
