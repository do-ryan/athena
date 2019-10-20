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
# import pdb; pdb.set_trace()


def string_to_inverse_suffix_array(string):
    # inverse suffix array has suffix index as index and rank as value
    # suffix array has rank as index and suffix index as value
    char_lexi_dict = {char: i for i, char in enumerate(sorted(string))}
    char_lexi_order = [char_lexi_dict[char] for char in string]
    suffix_array = suffix_sort_recurse(order_list=char_lexi_order, order_list_range=1)
    return suffix_array


def invert_suffix_array(suffix_array):
    inverse_suffix_array = [0]*len(suffix_array)
    for i, order in enumerate(suffix_array):
        inverse_suffix_array[order] = i
    return inverse_suffix_array


def lcp_array_construction(string, suffix_array, inverse_suffix_array):
    """Use Kasai's algorithm to construct LCP from suffix array. O(n)"""
    l = 0  # stores the global largest lcp
    lcp = [0]*len(suffix_array)
    for i in range(len(string)):  # start from biggest suffix
        k = inverse_suffix_array[i]  # get rank from current suffix index
        if (k+1) < len(string):
            j = suffix_array[k+1]  # get suffix index from next rank
        else:
            lcp[k] = 0
            continue
        while string[i:i+l+1] == string[j:j+l+1]:  # this gets the lcp to the next suffix.
            l += 1  # l can be max n and decremented at most n times. O(2n) total.
        lcp[k] = l
        if l > 0:
            l -= 1  # intuition here is that after we have encountered the largest lcp,
            # we will only encounter subsets of this lcp as we progress through i.
            # we do not encounter lcps with superset cps because we progress to smaller suffixes through i.
    return lcp


def counting_sort(lis):
    count = [0]*(max(lis) + 1)
    cumulative = [0]*len(count)
    for item in lis:
        count[item] += 1

    for i, frequency in enumerate(count):
        if i < len(count) - 1:
            cumulative[i+1] = cumulative[i] + frequency

    output = [0]*len(lis)

    for item in lis:
        output[cumulative[item]] = item
        cumulative[item] += 1

    return output


def suffix_sort_recurse(order_list: list, order_list_range: int):
    """Sort suffixes via recursively compounding in size all characters. O(nlogn)"""
    string_length = len(order_list)
    if len(set(order_list)) == string_length:
        return order_list
    next_order_list = [(order, order_list[i+order_list_range]) if (i+order_list_range < len(order_list))
                       else (order, -1) for i, order in enumerate(order_list)]
    sort_index = {tup: i for i, tup in enumerate(sorted(next_order_list))}
    # TODO: currently O(nlog^2n). Implement radix sort for O(nlogn)
    next_order_list = [sort_index[tup] for tup in next_order_list]
    return suffix_sort_recurse(next_order_list, order_list_range*2)


if __name__ == "__main__":
    strings = [input() for i in range(int(input()))]
    for string in strings:
        inverse_suffix_array = string_to_inverse_suffix_array(string)
        suffix_array = invert_suffix_array(inverse_suffix_array)
        n_duplicate_substrings = sum(lcp_array_construction(string, suffix_array, inverse_suffix_array))
        n = len(string)
        n_non_distinct_substrings = n*(n+1)//2 + 1
        print(n_non_distinct_substrings - n_duplicate_substrings)
