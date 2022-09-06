# 100 stones, random weights 0-10
# backpack limit is 30
# maximize weight in backpack without exceeding

import gurobipy as gp
from gurobipy import GRB, quicksum
import random

model = gp.Model('knapsack')

# sets
# set S is stones

# parameter
# w_s is weight of stone s for s in S
# L = capacity of backpack
# N = number of stones

# variables
# x_s is 1 iff stone s is in the backpack

# objective
# maximize sum of x_s*w_s over s

# constraint
# sum of x_s*w_s <= L
# x_s is a binary

N = 100

S = [s for s in range(N)]
w_s = [random.randint(0, 11) for _ in range(N)] 
L = 30

x_s = model.addVars(S, vtype=GRB.BINARY, name="x_s")

model.addConstr(quicksum(x_s[s]*w_s[s] for s in S) <= L)

model.setObjective(quicksum(x_s[s]*w_s[s] for s in S), GRB.MAXIMIZE)

model.optimize()
print([x_s[s].x for s in S])
