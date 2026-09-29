class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = [0] * len(height)
        highestSeen = 0

        for index, num in enumerate(height):
            highestSeen = max(highestSeen, height[index])
            leftMax[index] = highestSeen
        
        rightMax = [0] * len(height)
        highestSeen = 0

        for index in range(len(height)-1, -1, -1):
            highestSeen = max(highestSeen, height[index])
            rightMax[index] = highestSeen

        sumWater = 0
        for index in range(len(height)):
            sumWater += min(leftMax[index], rightMax[index]) - height[index]

        return sumWater
