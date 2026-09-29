class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [1] * len(nums)
        suffixes = [1] * len(nums)
        results = [1] * len(nums)

        for index in range(1, len(nums)):
            prefixes[index] = prefixes[index-1] * nums[index-1]
        
        for index in range(len(nums) - 2, -1, -1):
            suffixes[index] = suffixes[index+1] * nums[index+1]

        for index in range(len(nums)):
            results[index] = prefixes[index] * suffixes[index]

        return results