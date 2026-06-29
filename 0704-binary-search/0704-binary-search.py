class Solution:
    def search(self, nums: List[int], target: int) -> int:
        p = 0
        q = len(nums) - 1

        while p <= q:
            mid = (p + q) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                p = mid + 1
            else:
                q = mid - 1

        return -1