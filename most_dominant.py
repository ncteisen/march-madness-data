#!/usr/bin/env python3
"""What's the earliest round in which all 1 seeds were eliminated"""

import sys

from utils import sum_for_game, get_flattened_games

def get_winner(year, game_years):
    rnd = 2
    games = [g for g in game_years if 
                 g[0][0]["round_of"] == rnd and g[1] == year]
    assert(len(games) == 1)
    game = games[0]
    t1 = game[0][0]
    t2 = game[0][1]

    return t1 if t1["score"] > t2["score"] else t2

def get_dom_score(winner, year, game_years):
    diffs = []
    for rnd in (64, 32, 16, 8, 4, 2):
        games = [g for g in game_years if 
            g[0][0]["round_of"] == rnd and g[1] == year and 
            (g[0][0]["team"] == winner["team"] or 
                g[0][1]["team"] == winner["team"])]
        assert(len(games))
        game = games[0]
        diffs += [abs(game[0][0]["score"] - game[0][1]["score"])]
    return min(diffs)

def main():
    game_years = get_flattened_games(sys.argv[1:])
    years = set([gy[1] for gy in game_years])

    scores = []
    for year in years:
        winner = get_winner(year, game_years)
        dom_score = get_dom_score(winner, year, game_years)
        print("Year %d (%s): %d" % (year, winner["team"], dom_score))

if __name__ == '__main__':
    main()
