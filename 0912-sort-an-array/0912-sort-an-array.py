import random

class Solution:
    def sortArray(self, nums):

        def quicksort(l, r):
            if l >= r:
                return

            pivot = nums[random.randint(l, r)]

            lt = l      # nums[l..lt-1] < pivot
            i = l       # current element
            gt = r      # nums[gt+1..r] > pivot

            while i <= gt:
                if nums[i] < pivot:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1
                elif nums[i] > pivot:
                    nums[gt], nums[i] = nums[i], nums[gt]
                    gt -= 1
                else:
                    i += 1

            quicksort(l, lt - 1)
            quicksort(gt + 1, r)

        quicksort(0, len(nums) - 1)
        return nums