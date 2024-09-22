class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(0, len(nums)-1):
            for j in range(1, len(nums)):
                if nums[j] < nums[i] and j>i:
                    nums[i],nums[j] = nums[j],nums[i]
