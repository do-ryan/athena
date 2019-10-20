'''
The Triangle
            7
          3   8
        8   1   0
      2   7   4   4
    4   5   2   6   5   (Figure 1)
Figure 1 shows a number triangle. Write a program that calculates the highest sum of numbers passed on a route that starts at the top and ends somewhere on the base.

Each step can go either diagonally down to the left or diagonally down to the right.
The number of rows in the triangle is > 1 but ≤ 100.
The numbers in the triangle, all integers, are between 0 and 99 inclusive.
Input Format
The first line of input contains the integer n, the number of lines in the triangle. The remaining n lines will contain the values of the triangle.

Output Format
The output should contain one integer, the highest possible sum.

Sample Input
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
Sample Output
30
'''

def inp():
    n = int(input())
    triangle = []
    for _ in range(n):
        triangle.append([int(num) for num in input().split(' ')]) 
    return triangle


if __name__ == '__main__':
    triangle = inp()
    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            if len(triangle[i]) == 1:
                break
            elif j == 0:
                triangle[i][j] += triangle[i-1][0]
            elif j == len(triangle[i]) -1:
                triangle[i][j] += triangle[i-1][-1]
            else:
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])
    print(max(triangle[-1]))
