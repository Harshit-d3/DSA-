class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(capacity):
            daysNeeded = 1
            currWeight = 0

            for weight in weights:
                if currWeight + weight > capacity:
                    daysNeeded += 1
                    currWeight = 0
                currWeight += weight

            return daysNeeded <= days

        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2

            if canShip(mid):
                right = mid
            else:
                left = mid + 1

        return left