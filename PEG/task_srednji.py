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
# import pdb; pdb.set_trace()


def inp():
    length, median = (int(char) for char in input().split(' '))
    sequence = input().split(' ')
    return median, sequence


def median_in_list(lis, median):
    delta = 0
    for item in lis:
        if item > median:
            delta += 1
        elif item < median:
            delta -= 1
    return delta == 0


def rec_count_subseq_median(sequence, median, start, end):
    if start < 0 or end >= len(sequence):
        return 0
    return count_subseq_median(sequence, median, start - 1, end + 1) \
        + count_subseq_median(sequence, median, start, end + 2) \
        + count_subseq_median(sequence, median, start - 2, end) \
        + median_in_list(sequence[start:end+1], median)


def delta_function(sequence, median):
    return sum([1 if integer > median else -1 for integer in sequence])


def count_subseq_median(sequence, median, median_i):
    delta_l = []
    delta_r = []
    num_subseq = 0
    for i in range(median_i-1, -1, -1):
        if sequence[i] < median:
            delta = -1
        else:
            delta = 1
        if delta_l:
            delta_l.append(delta + delta_l[-1])
        else:
            delta_l.append(delta)
        if delta_l[-1] == 0:
            num_subseq += 1
    for i in range(median_i+1, len(sequence)):
        if sequence[i] < median:
            delta = -1
        else:
            delta = 1
        if delta_r:
            delta_r.append(delta + delta_r[-1])
        else:
            delta_r.append(delta)
        if delta_r[-1] == 0:
            num_subseq += 1
        #for d_l in delta_l:
        #    if d_l + delta_r[-1] == 0:
        #        num_subseq += 1
    return num_subseq + 1  # for the trivial case


if  __name__ == '__main__':
    median, char_sequence = inp()
    sequence = []
    median_i = None

    for i, num in enumerate(char_sequence):
        sequence.append(int(num))
        if sequence[len(sequence) - 1] == median:
            median_i = i

    if median_i is not None:
        print(count_subseq_median(sequence, median, median_i))
    else:
        print(0)
