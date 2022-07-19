# 100 rocks, each has a weight
# maximize weight in bag while fulfilling capacity

from typing import List

def knapsack(weights: List[int], limit: int):
    
    current_max = 0 
    limit = 30
    
    def recurse(decisions: list): 
        global current_max
        if len(decisions) > 0:
            current_total_weight = sum([weights[i] for i, decision in enumerate(decisions) if decision == 1]) 
            if len(decisions) == len(weights): 
                current_max = max(current_max, current_total_weight)
                return
            if current_total_weight > limit:
                decisions[-1] = 0
                current_max = max(current_max, current_total_weight)

        recurse(decisions + [0])
        recurse(decisions + [1])

    recurse([]) 

    return current_max

