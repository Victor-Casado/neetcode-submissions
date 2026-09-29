class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #for any 2 nums, we can know target, the num that would complete the triplet
        targetNums = {} #target -> [[idx 1, idx2], [idx 1, idx2]]
        returner = set()

        for currentIndex, num in enumerate(nums):
            if (targetNums.get(num) != None):
                for indices in targetNums[num]:
                    returner.add(tuple(sorted((indices + [num]))))
                targetNums.pop(num)
            
            for prevNum in nums[:currentIndex]:
                if (targetNums.get(0-num-prevNum) != None):
                    targetNums[0-num-prevNum].append([num, prevNum])
                else:
                    targetNums[0-num-prevNum] = [[num, prevNum]]
        
        return [list(x) for x in returner]