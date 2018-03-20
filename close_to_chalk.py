#!/usr/bin/env python3
"""What's the earliest round in which all 1 seeds were eliminated"""

import sys

from utils import sum_for_game, get_flattened_games

_ROUNDS_SCORES = [
    (64, 10),
    (32, 20),
    (16, 40),
    (8, 80),
    (4, 160),
    (2, 320),
]

def chalk(game, c_range):
    t1 = game[0][0]
    t2 = game[0][1]

    winner = t1 if t1["score"] > t2["score"] else t2
    loser = t1 if t1["score"] < t2["score"] else t2

    # print ("%s (%d) beat %s (%d), which %s chalk" % (
    #     winner["team"], winner["seed"], 
    #     loser["team"], loser["seed"], 
    #     "is" if winner["seed"] in c_range else "is not"))

    return winner["seed"] in c_range

def get_score(game_years, year):
    score = 0
    for i, rnd_scr in enumerate(_ROUNDS_SCORES):
        rnd = rnd_scr[0]
        scr = rnd_scr[1]
        games = [g for g in game_years if 
                 g[0][0]["round_of"] == rnd and g[1] == year]
        r = range(1, (16/(i+2))+1)
        for g in games:
            if chalk(g, r):
                score += scr
    return score


def main():
    game_years = get_flattened_games(sys.argv[1:])
    years = set([gy[1] for gy in game_years])

    scores = []
    for year in years:
        scores += [(year, get_score(game_years, year))]

    scores = sorted(scores, key=lambda x: x[1])
    for s in scores:
        print s


if __name__ == '__main__':
    main()
