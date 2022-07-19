"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);


Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"


Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 1. Get number of columns and build array
        # 2. map letter to array
        # 3. print array row wise

        if numRows == 1:
            return s

        # 1. a. number of cols:
        num_cols = 0
        letter_count = 0
        while letter_count < len(s):
            letter_count += numRows
            num_cols += 1
            for _ in range(numRows - 2):
                letter_count += 1
                num_cols += 1
                if letter_count >= len(s):
                    break

        array = [['' for _ in range(num_cols)] for _ in range(numRows)]


        # 2. map letter to array
        curr_row_i = 0
        curr_col_i = 0
        direction_up = False

        for i, char in enumerate(s):
            array[curr_row_i][curr_col_i] = char
            if not direction_up:
                if curr_row_i + 1 < numRows:
                    curr_row_i += 1
                else:
                    direction_up = True
                    curr_col_i += 1
                    curr_row_i -= 1
            else:
                if curr_row_i > 0:
                    curr_col_i += 1
                    curr_row_i -= 1
                else:
                    direction_up = False
                    curr_row_i += 1

        ret_string = ''
        for i in range(numRows):
            for j in range(num_cols):
                if array[i][j] != '':
                    ret_string += array[i][j]

        return ret_string
