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
    def __init__(self):
        self.edges = {}

    def add_edge(self, n1, n2):
        if n1 not in self.edges:
            self.edges[n1] = [n2]
        else:
            self.edges[n1].append(n2)
        
        if n2 not in self.edges:
            self.edges
