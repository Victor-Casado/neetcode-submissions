class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_found = {}
        for num in nums:
            if (nums_found.get(num) != None):
                return True
            nums_found[num] = 1
        return False