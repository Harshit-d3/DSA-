from collections import defaultdict
from bisect import bisect_right

class TimeMap:

    def __init__(self):
        self.mp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mp:
            return ""

        arr = self.mp[key]

        # Find first index with timestamp > given timestamp
        idx = bisect_right(arr, timestamp, key=lambda x: x[0])

        if idx == 0:
            return ""

        return arr[idx - 1][1]