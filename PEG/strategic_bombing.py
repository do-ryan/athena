"""
2001 Canadian Computing Competition, Stage 1
Problem J5/S3: Strategic Bombing
The Enemy relies heavily on the transportation of supplies and personnel between the specific points A and B.
Points A and B, as well as other points C, D, E, etc. are linked by a network of roads.
Your mission, should you accept it, is to identify a single road that may be bombed in order to cut off all
traffic between A and B.

Input
In the input, each point is identified by a single upper-case letter (there are a maximum of 26 points).
Each line of input identifies a pair of points connected by a road.

The end of input is indicated by a line containing "**". All roads are two-way, that is, road AC is the same as road CA.
There is at most one road between any pair of points.

Output
Your output should identify all roads such that bombing any one of them would halt all traffic between A and B. Your output should list the roads, one per line, followed by a line stating that "There are n disconnecting roads.", where n is the number of such roads.

If there is no such road, output "There are 0 disconnecting roads."

Sample Input
AC
AD
AE
CE
CF
ED
GF
BG
HB
GH
**

Sample Output
CF
GF
There are 2 disconnecting roads.
"""


class UndirectedGraph():
    """Mutable class. States can be changed externally."""
    def __init__(self):
        self.neighbours = {}

    def add_edge(self, n1, n2):
        if n1 not in self.neighbours:
            self.neighbours[n1] = [n2]
        else:
            self.neighbours[n1].append(n2)
        
        if n2 not in self.neighbours:
            self.neighbours[n2] = [n1]
        else:
            self.neighbours[n2].append(n1)

     def 

def inp(roads_graph):
    entry = input()
    while entry != "**":
        roads_graph.add_edge(entry[0], entry[1])
        entry = input()


if __name__ == "__main__":
"""
    Approaches:
        1. Use DFS to find all possible paths from A to B. Intersection of nodes between A and B are crucial paths: superpolynomial
	2. Cycle detection? No, doesn't work. We end up finding non cycle nodes that are needed to get to B using approach 1 but explicitly looking for nodes not in cycles won't necessarily give nodes that are needed to get to B. 
        3. Remove edges one by one and run DFS to determine if edge is a bridge from A to B. O(V*(E+V))`
        4. Finding bridges: general bridge searching with traversal time. But only for path from A to B which is searched first. The current edge (v,to) is a bridge if and only if none of the vertices to and its descendants in the DFS edge traversal tree has a back-edge to vertex v or any of its ancestors. Indeed, this condition means that there is no other way from v to to except for edge (v,to).
        low[v]=min⎧⎩⎨⎪⎪tin[v]tin[p]low[to] for all p for which (v,p) is a back edge for all to for which (v,to) is a tree edge. If low[to] > tin[v] then (v, to) is a bridge. The intuition is that if tin[v] >= low[to] then v has been reached by a back edge. If tin[v] == low[to] then to goes directly to v via back edge. https://cp-algorithms.com/graph/bridge-searching.html
"""
    roads_graph = UndirectedGraph()
    inp(roads_graph)


