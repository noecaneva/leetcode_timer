class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        stack = []
        ans = [0] * n

        # Stack tracks the current highest temp
        for i in range(n-1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            ans[i] = stack[-1] - i if stack else 0
            stack.append(i)

        return ans

def solve_stack(temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        stack = []
        ans = [0] * n

        # Stack tracks the current highest temp
        for i in range(n-1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            ans[i] = stack[-1] - i if stack else 0
            stack.append(i)

        return ans

SOLUTIONS = {
    "stack": solve_stack,
}