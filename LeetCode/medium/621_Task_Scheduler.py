"""
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.



Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation:
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.
Example 2:

Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.
Example 3:

Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation:
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A


Constraints:

1 <= task.length <= 104
tasks[i] is upper-case English letter.
The integer n is in the range [0, 100].
"""

from collections import defaultdict

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # at any point in time, choose the task that minimizes actual cooldown.
        # keep track of task with highest task count
        # at each time step, choose task with highest task count with cooldown greater than or equal to n.
        # if none greater than n, idle and increase all cooldowns by 1
        current_time = 0
        dict_current_cd = {}
        dict_task_count = defaultdict(int)
        for task in tasks:
            dict_current_cd[task] = n + 1
            dict_task_count[task] += 1
        highest_count_task = max(tasks, key=lambda x: dict_task_count[x])

        while sum(dict_task_count.values()) > 0:
            ready_tasks = {task for task in tasks if dict_current_cd[task] > n and dict_task_count[task] > 0}
            if ready_tasks:
                highest_count_task = max(ready_tasks, key=lambda x: dict_task_count[x])
                dict_current_cd[highest_count_task] = 0
                dict_task_count[highest_count_task] -= 1
            for task in dict_current_cd.keys():
                dict_current_cd[task] += 1
            current_time += 1
            print(highest_count_task, dict_current_cd, dict_task_count)

        return current_time


