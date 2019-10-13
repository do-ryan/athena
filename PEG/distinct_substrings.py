"""
2003 Canadian Computing Competition, Stage 1
Problem S4: Substrings
How many distinct substrings does a given string S have?

For example, if S = "abc", S has 7 distinct substrings: "", "a", "b", "c", "ab", "bc", "abc".
Note that the empty string and S itself are considered substrings of s.

On the other hand, if S = "aaa". S has only 4 distinct substrings: "", "a", "aa", "aaa".

Input
The first line of the input file contains N, the number of test cases. For each test case, a line follows giving S,
a string of from 1 to 5000 alphanumeric characters.

Output
Your output consists of one line per case, giving the number of distinct substrings of S.

Grading
50% of test cases will have l (the length of the string) ≤ 1,000.
For all cases, l ≤ 5000.
Sample Input
2
abc
aaa
Sample Output
7
4
"""
#import pdb; pdb.set_trace()

def inp():
    N = int(input())
    strings = [input() for i in range(N)]
    return strings

def string_to_suffix_array(string):
    char_lexi_order = [ord(char) for char in string]
    suffix_order = suffix_sort_recurse(order_list=char_lexi_order, order_list_range=1)
    suffix_array = [string[i:]  for i in range(-len(string), 0)]
    sorted_suffix_array = [0]*len(suffix_array)
    for i, order in enumerate(suffix_order):
        sorted_suffix_array[order] = suffix_array[i]
    return sorted_suffix_array

def suffix_sort_recurse(order_list: list, order_list_range: int):
    if order_list_range > len(order_list) or len(set(order_list)) == len(order_list):  # first condition redundant because first condition guarantees second condition
        return order_list
    next_order_list = [(order, order_list[i+order_list_range]) if (i+order_list_range < len(order_list)) else (order, -1) for i, order in enumerate(order_list)]
    sort_index = {tup: i for i, tup in enumerate(sorted(next_order_list))}
    next_order_list = [sort_index[tup] for tup in next_order_list]
    return suffix_sort_recurse(next_order_list, order_list_range*2)


if __name__ == "__main__":
    strings = inp()
    for string in strings:
        print(string_to_suffix_array(string))
