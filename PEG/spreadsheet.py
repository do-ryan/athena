"""
2004 Canadian Computing Competition, Stage 1
Problem S3: Spreadsheet
A spreadsheet consists of a number of "cells" set in a rectangular grid. Each is addressed with one letter from A to J
(giving the row) and one number from 1 to 9 (giving the column).
Thus the upper-left cell of the spreadsheet is A1, and the lower-right cell is J9.

Every cell has a value, and this can be specified in one of two ways:

as an integer from 0 to 1000
as a sum of the values of up to 10 other cells
Cell values may be interdependent (that is, A1's sum may depend on B6 which depends on C9),
but a cell whose value depends on itself, directly or indirectly, is undefined
(e.g., A1 depending on G8 depending on A1). Also, a cell whose value depends on an undefined cell is itself undefined.

You are given the specification for all the cells in the spreadsheet. Compute and output the values of all of the cells.

Input
Input will consist of 10 lines, one per spreadsheet row.

Each line contains 9 descriptions of a cell, which will be either an integer between 0 and 1000, or a sum of 1 to 10
distinct cell names separated by a "+" symbol (e.g. "A1+B5+D3").

Output
Output 10 lines, with 9 numbers per line, giving the value of every cell in the spreadsheet;
if the cell is undefined, print an asterisk (*) in place of its value. 
No cell's final value will exceed 1 000 000 000.


Sample Input
1 2 3 A1+A2+A3 A3+A4 A1+A4+A5 A8+A9 A9 A8
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
Sample Output
1 2 3 6 9 16 * * *
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
"""
