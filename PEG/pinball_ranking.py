"""
Problem S5: Pinball Ranking
Pinball is an arcade game in which an individual player controls a silver ball by means of flippers,
with the objective of accumulating as many points as possible. At the end of each game,
the player's score and rank are displayed. The score, an integer between 0 and 1 000 000 000,
is that achieved by the player in the game just ended. The rank is displayed as "r of n".
n is the total number of games ever played on the machine,
and r is the position of the score for the just-ended game within this set.

More precisely, r is one greater than the number of games whose score exceeds that
of the game just ended.

Input
You are to implement the pinball machine's ranking algorithm.
The first line of input contains a positive integer, t, the total number of games
played in the lifetime of the machine. t lines follow, given the scores of these games,
in chronological order.

Output
You are to output the average of the ranks (rounded to two digits after the decimal)
that would be displayed on the board.
At least one test case will have t ≤ 100. All test cases will have t ≤ 100 000.

Sample Input
5
100
200
150
170
50
Sample Output
2.20
Explanation
The pinball screen would display (in turn):

1 of 1
1 of 2
2 of 3
2 of 4
5 of 5
The average rank is (1+1+2+2+5)/5 = 2.20.
"""


def inp():
    n = int(input())
    return [int(input()) for i in range(n)]


def compute_ranks(scores, score_rank_dict):
    def merge_generator(list_l, list_r):
        n_left_merge = 0
        while list_l or list_r:
            if not list_l:
                score_rank_dict[list_r[-1]] = (score_rank_dict[list_r[-1]][0], score_rank_dict[list_r[-1]][1]
                                               - n_left_merge)
                yield list_r.pop()
            elif not list_r:
                n_left_merge += 1
                yield list_l.pop()
            elif score_rank_dict[list_l[-1]][0] <= score_rank_dict[list_r[-1]][0]:
                n_left_merge += 1
                yield list_l.pop()
            else:
                score_rank_dict[list_r[-1]] = (score_rank_dict[list_r[-1]][0], score_rank_dict[list_r[-1]][1]
                                               - n_left_merge)
                yield list_r.pop()
    if len(scores) == 1:
        return scores
    scores_l = compute_ranks(scores[0:len(scores) // 2], score_rank_dict)
    scores_r = compute_ranks(scores[len(scores) // 2:], score_rank_dict)
    scores_l.reverse()
    scores_r.reverse()
    return [score for score in merge_generator(scores_l, scores_r)]


if __name__ == '__main__':
    """
    Notes:
        - Need to preserve order of insertion.

    Approaches:
        - Sequentially insert into sorted list ordered by descending and keep track of rank and n.
            - O(n^2)
        - Merge sort.
            - Bottom-up: each score is hash-mapped to its insertion order y. This is y in x of y
            100:1 - 200:2 - 150:3 - 170:4 - 50:5
            100:1  200:1 - 150:3 170:3 - 50:5
            100:1 200:1 - 50:5 150:3 170:3
            50:5 100:1 150:2 170:2 200:1
                - if a score is on the right side of merge, every time a left element is merged before it, decrease score:y by 1. A newer equal score is considered greater.
                    - proof: when an element is on the right side of a merge it is being inserted in sorted order to all those before it (on the left side of a merge). The number of left side merge-ins before the element is its number of ranks above last place, therefore subtracting 1 for each from the element's current last place (at time of its record) gives its rank.
           - O(nlog(n))
    """
    scores = inp()
    score_rank_dict = {i: (score, i + 1) for i, score in enumerate(scores)}
    compute_ranks(list(score_rank_dict.keys()), score_rank_dict)
    ranks = [rank for score, rank in score_rank_dict.values()]
    print(str('{0:.2f}'.format(sum(ranks)/len(score_rank_dict.values()))))
