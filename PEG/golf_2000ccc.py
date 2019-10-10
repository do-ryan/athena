"""
Roberta the Robot plays a perfect game of golf.
When she hits the golf ball it always goes directly towards the hole on the green,
and she always hits exactly the distance that is specified for the club.
Each such action is known as a stroke, and the object of golf is to hit the ball from the tee to
the hole in the fewest number of strokes. Roberta needs a program to select the best combination of clubs
to reach the hole in the fewest strokes. She also needs to decide if the task is impossible,
in which case she graciously acknowledges the loss. Roberta can carry up to 32 clubs,
and the total distance from the tee to the hole does not exceed 5280 metres.

Input
The first line of input gives the distance from the tee to the hole, an integral number of metres between 1 and 5280.
The next line states the number of clubs, between 1 and 32. For each club, a line follows giving the distance,
in metres, that the club will hit the ball, an integer between 1 and 100. No two clubs have the same distance.

Output
If Roberta can get the ball from the tee to the hole, without passing the hole, print "Roberta wins in n strokes."
where n is minimized. If Roberta cannot get the ball from the tee to the hole, print "Roberta acknowledges defeat.".

Sample Input
100
3
33
66
1
Sample Output
Roberta wins in 3 strokes.
"""
# import datetime


def inp():
    """Return list of integers from problem input"""
    dist = int(input())
    n_clubs = int(input())
    club_dist = [int(input()) for _ in range(n_clubs)]
    return dist, n_clubs, club_dist


def num_strokes(dist, club_dist):

    best_strokes = [9999] * dist

    for this_dist, best_stroke in enumerate(best_strokes):
        for club in club_dist:
            if club == (this_dist + 1):
                best_strokes[this_dist] = 1
            else:
                if (this_dist + 1) - club >= 0:
                    best_strokes[this_dist] = min(
                        best_strokes[this_dist], best_strokes[this_dist - club] + 1)

    return best_strokes[dist - 1]


if __name__ == "__main__":
    dist, n_clubs, club_dist = inp()
    res = num_strokes(dist, club_dist)
    if res != 9999:
        print("Roberta wins in", res, "strokes.")
    else:
        print("Roberta acknowledges defeat.")
