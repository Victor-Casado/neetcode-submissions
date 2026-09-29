class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        maxFound = 0

        while(left != right):
            water = (right - left) * min(heights[left], heights[right])
            maxFound = max(maxFound, water)

            if(heights[left] < heights[right]):
                left += 1
            else:
                right -= 1

        return maxFound
            