"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.


Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""
from collections import defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Uses topological sort. 
        # 1. Build prerequisite graph as dict
        # 2. Queue all courses with no prereq
        # 3. For each course visited, decrease neighbours' indegrees by 1. Only add neighbour to queue if indegree is 0.
        prereq_graph = defaultdict(list)
        indegree_dict = defaultdict(int)
        for i, prereq in enumerate(prerequisites):
            prereq_graph[prereq[1]].append(prereq[0])
            indegree_dict[prereq[0]] += 1
        noprereq_courses = {course for course in range(numCourses) if indegree_dict[course] == 0}

        bfs_queue = []
        visited_courses = set()
        bfs_queue += list(noprereq_courses)
        for course in bfs_queue:
            visited_courses.add(course)
            for neighbour in prereq_graph[course]:
                indegree_dict[neighbour] -= 1
                if indegree_dict[neighbour] == 0:
                    bfs_queue.append(neighbour)

        if len(visited_courses) == numCourses:
            return True
        return False
