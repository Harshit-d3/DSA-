class Solution:
    def maxScore(self, s: str) -> int:
        ones = s.count('1')
        zeros = 0
        ans = 0

        # Split between i and i+1
        # So the last character cannot be included in the left part.
        for i in range(len(s) - 1):
            if s[i] == '0':
                zeros += 1
            else:
                ones -= 1

            ans = max(ans, zeros + ones)

        return ans