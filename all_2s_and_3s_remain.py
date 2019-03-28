#!/usr/bin/env python3

import sys

from utils import sum_for_game, get_flattened_games

def count_2s_and_3s(games):
    count = 0
    for g in games:
        if g[0][0]["seed"] == 2 or g[0][1]["seed"] == 2:
            count += 1
        if g[0][0]["seed"] == 3 or g[0][1]["seed"] == 3:
            count += 1
    return count

def main():
    game_years = get_flattened_games(sys.argv[1:])
    years = set([gy[1] for gy in game_years])

    for year in years:
        for rnd in (64, 32, 16, 8, 4, 2):
            games = [g for g in game_years if 
                     g[0][0]["round_of"] == rnd and g[1] == year]
            num_2s_and_3s = count_2s_and_3s(games)
            if num_2s_and_3s == 8:
                if rnd != 64:
                    print("In %d, all twos and threes remained in the round of %d" % (year, rnd))
            else:
                break


if __name__ == '__main__':
    main()
