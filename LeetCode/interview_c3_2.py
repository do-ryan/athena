# 100 rocks, each has a weight
# maximize weight in bag while fulfilling capacity

from typing import List

def knapsack(weights: List[int], limit: int):
    
    global current_max
    global best_solution
    current_max = 0
    
    def recurse(decisions: list): 
        global current_max
        global best_solution
        if len(decisions) > 0:
            current_total_weight = sum([weights[i] for i, decision in enumerate(decisions) if decision == 1]) 
            if current_total_weight > limit:
                decisions[-1] = 0
                current_total_weight = sum([weights[i] for i, decision in enumerate(decisions) if decision == 1]) 
                if current_total_weight >= current_max:
                    best_solution = decisions
                    current_max = current_total_weight
                    print(decisions)
            if len(decisions) == len(weights): 
                if current_total_weight >= current_max:
                    best_solution = decisions
                    current_max = current_total_weight
                return

        recurse(decisions + [0])
        recurse(decisions + [1])

    recurse([]) 

    return current_max, best_solution

