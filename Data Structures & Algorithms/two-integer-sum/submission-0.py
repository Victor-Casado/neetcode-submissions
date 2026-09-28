class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {} #[number] -> index
        
        for index, num in enumerate(nums):
            if(indices.get(target - num) != None):
                return [indices.get(target - num), index]
            indices[num] = index
