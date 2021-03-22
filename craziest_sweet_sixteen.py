#!/usr/bin/env python3

import sys

from utils import sum_for_game, get_flattened_games

def count_seeds(games):
    count = 0
    for g in games:
        count += g[0][0]["seed"]
        count += g[0][1]["seed"]
    return count

def main():
    game_years = get_flattened_games(sys.argv[1:])
    years = set([gy[1] for gy in game_years])

    final = []
    for year in years:
        rnd = 16
        games = [g for g in game_years if 
                 g[0][0]["round_of"] == rnd and g[1] == year]
        seeds = count_seeds(games)
        final += [(year, seeds)]
    final = sorted(final, key=lambda x: x[1])
    print(final)


if __name__ == '__main__':
    main()
