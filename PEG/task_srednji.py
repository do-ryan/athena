"""
COCI 2007/2008, Contest #1
Task SREDNJI
Consider a sequence A of integers, containing N integers between 1 and N.
Each integer appears exactly once in the sequence.

A subsequence of A is a sequence obtained by removing some (possibly none) numbers from the beginning of A,
and then from the end of A.

Calculate how many different subsequences of A of odd length have their median equal to B.
The median of a sequence is the element in the middle of the sequence after it is sorted.
For example, the median of the sequence {5, 1, 3} is 3.

Input
The first line contains two integers, N (1 ≤ N ≤ 100 000) and B (1 ≤ B ≤ N).

The second line contains N integers separated by spaces, the elements of sequence A.

Output
Output the number of subsequences of A whose median is B.

Examples
Input
5 4
1 2 3 4 5
Output
2

Input
6 3
1 2 4 5 6 3
Output
1

Input
7 4
5 7 2 4 3 1 6
Output
4

In the fourth example, the four subsequences of A with median 4 are
{4}, {7, 2, 4}, {5, 7, 2, 4, 3} and {5, 7, 2, 4, 3, 1, 6}.
"""
# import pdb
# pdb.set_trace()


def inp():
    length, median = (int(char) for char in input().split(' '))
    sequence = input().split(' ')
    return median, sequence


def count_subseq_median(sequence, median, start, end, new_indices, num_bigger, num_smaller):
    if start < 0 or end >= len(sequence):
        return 0
    num_bigger += sum([sequence[new_index] > median for new_index in new_indices])
    num_smaller += sum([sequence[new_index] < median for new_index in new_indices])
    return count_subseq_median(sequence, median, start - 1, end + 1, [start - 1, end + 1], num_bigger, num_smaller) \
        + count_subseq_median(sequence, median, start, end + 2, [end + 1, end + 2], num_bigger, num_smaller) \
        + count_subseq_median(sequence, median, start - 2, end, [start - 1, start - 2], num_bigger, num_smaller) \
        + (num_bigger == num_smaller)


if __name__ == '__main__':
    median, char_sequence = inp()
    sequence = []
    median_i = None

    for i, num in enumerate(char_sequence):
        sequence.append(int(num))
        if sequence[len(sequence) - 1] == median:
            median_i = i

    if median_i is not None:
        print(count_subseq_median(sequence, median, median_i, median_i, [], 0, 0))
    else:
        print(0)
