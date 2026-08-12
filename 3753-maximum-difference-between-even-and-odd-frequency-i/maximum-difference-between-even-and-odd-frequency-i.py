class Solution:
    def maxDifference(self, s: str) -> int:
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        max_odd = 0
        min_even = float('inf')

        for f in freq:
            if f == 0:
                continue

            if f % 2 == 1:
                max_odd = max(max_odd, f)
            else:
                min_even = min(min_even, f)

        return max_odd - min_even