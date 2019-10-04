"""
The school year has just begun, so it's time for Alice to find a suitable boyfriend! Naturally, this process will first
require some careful research using a convenient online academic source known as Facebook.

Alice is considering G (1 ≤ G ≤ 100) guys, and wants to estimate how well-matched she would be with each of them -
in other words, how attractive each of them is. For each guy, Alice can find N (1 ≤ N ≤ 100) pictures of him on
Facebook, the i-th of which has attractiveness Ai (1 ≤ Ai ≤ 100). The guy might be as ugly as his least-attractive
picture (the one with the smallest attractiveness value), or as hot as his most-attractive picture.

In making her important and complex decision, Alice would like to know the potential range of attractiveness of each of
the G potential guys!

Input
Line 1: 1 integer, G

For each guy:
Line 1: 1 integer, N
Line 2: N integers, A1..N

Output
For each guy, output 2 integers, the guy's worst-case and best-case attractiveness, respectively.

Sample Input
3
4
2 5 1 3
1
98
5
16 11 11 14 21
Sample Output
1 5
98 98
11 21
Explanation of Sample
The first guy's worst picture (his third) has attractiveness 1, while his best (his second) has attractiveness 5.
The second guy has only one picture, making his attractiveness definitely 98.
Finally, the third guy's worst-case attractiveness is 11 (with two of his pictures having this value),
while his best is 21.
"""

if __name__ == "__main__":
    num_guys = input()
    res = []
    for guy in range(int(num_guys)):
        num_photos = int(input())
        photo_scores = [int(i) for i in input().split(' ')]
        res.append((min(photo_scores), max(photo_scores)))
    for it in res:
        print(it[0], it[1])
