class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:
            if ch in pairs:  # Closing bracket
                if not stack or stack.pop() != pairs[ch]:
                    return False
            else:  # Opening bracket
                stack.append(ch)

        return len(stack) == 0
        