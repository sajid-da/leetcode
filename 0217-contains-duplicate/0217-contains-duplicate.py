class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        i=0
        j=1
        new = sorted(nums)
        while j<len(new):
            if new[i] == new[j]:
                return True

        
            i+=1
            j+=1
        
        return False


        
        