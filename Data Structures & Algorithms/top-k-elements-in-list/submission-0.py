class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_frequencies = {}

        for num in nums:
            if num in num_frequencies:
                num_frequencies[num] += 1
            else:
                num_frequencies[num] = 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, frequency in num_frequencies.items():
            buckets[frequency].append(num)

        returner = []

        for bucket in reversed(buckets):
            for num in bucket:
                returner.append(num)
                if len(returner) == k:
                    return returner
