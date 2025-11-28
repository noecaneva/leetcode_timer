from typing import List

def minCostClimbingStairs_vec(cost: List[int]) -> int:
    # This is a good DP solvable problem
    # the reason is that the minimum cost to arrive
    # at a step is immutable, meaning that it will not change
    # on top of that we have only up to 1000 stairs meaning we don't
    # have to worry about runtime too much
    N = len(cost)
    min_cost = [10000]*N
    min_cost[:2]=[0, 0]
    for i in range(2,N):
        min_cost[i] = min(min_cost[i-1]+cost[i-1], min_cost[i-2]+cost[i-2])
    
    return min(min_cost[N-1]+cost[N-1], min_cost[N-2]+cost[N-2])

def minCostClimbingStairs_3_num(cost: List[int]) -> int:
    # here we end up with the cost "to jump off of" the step
    min_cost_prev = 0
    min_cost_prev_prev = 0
    min_cost_to_arrive = 0
    N = len(cost)
    for i in range(2,N+1):
        min_cost_to_arrive = min(cost[i-1]+min_cost_prev, cost[i-2]+min_cost_prev_prev)
        min_cost_prev, min_cost_prev_prev = min_cost_to_arrive, min_cost_prev
    
    return min_cost_to_arrive

SOLUTIONS = {
    "min_cost_vector": minCostClimbingStairs_vec,
    "min_cost_3_num": minCostClimbingStairs_3_num,
}