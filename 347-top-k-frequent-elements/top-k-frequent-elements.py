from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequencies
        count = Counter(nums)

        # Buckets: index = frequency
        freq = [[] for _ in range(len(nums) + 1)]

        for num, c in count.items():
            freq[c].append(num)

        res = []

        # Traverse buckets from high frequency to low
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res