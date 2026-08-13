class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        j = 0
        
        for x in pushed:
            stack.append(x)
            # While the stack is not empty and the top matches the current popped element
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
                
        return not stack