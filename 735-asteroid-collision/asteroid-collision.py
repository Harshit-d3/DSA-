class Solution:
    def asteroidCollision(self, asteroids):
        stack = []

        for asteroid in asteroids:
            while stack and asteroid < 0 and stack[-1] > 0:
                if stack[-1] < -asteroid:
                    stack.pop()          # Right-moving asteroid explodes
                    continue
                elif stack[-1] == -asteroid:
                    stack.pop()          # Both explode
                break                    # Current asteroid explodes (or both exploded)
            else:
                stack.append(asteroid)

        return stack