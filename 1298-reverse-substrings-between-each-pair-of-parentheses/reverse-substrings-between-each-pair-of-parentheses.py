class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char == ')':
                # Extract characters inside the current pair of parentheses
                curr_chars = []
                while stack and stack[-1] != '(':
                    curr_chars.append(stack.pop())
                
                # Pop the opening bracket '('
                if stack and stack[-1] == '(':
                    stack.pop()
                
                # Push the reversed characters back onto the stack
                for c in curr_chars:
                    stack.append(c)
            else:
                stack.append(char)
                
        return "".join(stack)